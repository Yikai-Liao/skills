# 原生 CPU 性能分析工具链

用于 Linux 原生代码，尤其是可重复的 Intel x86 CPU 工作负载。主线是 **perf 定位真实热点 → toplev 判断硬件瓶颈类别 → 实际汇编/IR 与 LLVM-MCA 解释机制 → 实验裁决**。其他平台选对应的采样器、PMU 工具和架构模型，不强行套用 Intel 事件。

## 准备与工具来源

优先复用已安装工具，缺什么补什么。工具、venv、模型数据库放在独立分析目录，保存版本、仓库 commit 和命令。正在比较候选时不要顺便升级 libc、编译器或生产依赖；必要时独立解包工具包。不要仅因 VM 或 `perf_event_paranoid` 的数值就断言不可用，先做最小实测。

| 工具 | 获取与核对 |
|---|---|
| perf、objdump、nm | 系统 perf/binutils；`perf --version`、`perf list`，perf 包按发行版与内核选择 |
| toplev / ocperf | [PMU Tools](https://github.com/andikleen/pmu-tools)，可直接从 clone 运行；首次可能下载 CPU 事件表 |
| LLVM-MCA / llvm-exegesis | [LLVM 工具](https://llvm.org/docs/CommandGuide/)，命令可能带版本后缀；本例用已验证的 `-19` |
| Cachegrind / cg_annotate | [Valgrind](https://valgrind.org/docs/manual/cg-manual.html)，核对版本及程序支持情况 |
| uiCA | [上游源码](https://github.com/andreas-abel/uiCA)，在专用 clone 中执行 `setup.sh` 构建 XED 和模型 |
| OSACA | [上游源码与文档](https://github.com/RRZE-HPC/OSACA)，在独立 Python venv 中安装 |

按需准备补充模型的环境，例如 `python3 -m venv /path/to/tools/venv`，再用其 Python 执行 `-m pip install osaca plotly setuptools`。uiCA 的 setup 需要编译工具并下载/转换指令数据库；其子模块清理只应发生在专用 clone 中。不要为格式说明安装整套生产无关依赖。实际版本的 `--help` 和源仓库说明优先于以下示例。

以下是 Bash 模板。先把路径、输入和 CPU 换成实际值，保存完整命令；单线程例不代表必须把多线程目标改成单线程。

```bash
analysis_dir=/absolute/path/to/evidence
pmu_tools=/absolute/path/to/pmu-tools
uica_root=/absolute/path/to/uiCA
model_python=/absolute/path/to/tools/venv/bin/python
bench_cpu=2
binary=/absolute/path/to/bench
bench=("$binary" --case representative)
run=(taskset -c "$bench_cpu" "${bench[@]}")
mkdir -p "$analysis_dir"
lscpu > "$analysis_dir/lscpu.txt"
perf --version > "$analysis_dir/perf-version.txt"
perf stat -e cycles:u,instructions:u -- "${run[@]}"
```

确认事件非零、返回状态正确，目标确实做了工作。硬件计数不可用时仍可做可比的 wall/CPU 测量及静态分析；明确缺少哪一层证据，不擅自修改系统安全配置。

## 1. perf：先证明热点存在

```bash
perf stat -x, -o "$analysis_dir/stat.csv" \
  -e cycles:u,instructions:u,branches:u,branch-misses:u -- "${run[@]}"
perf record -o "$analysis_dir/perf.data" -F 499 -e cycles:u \
  --call-graph dwarf,4096 -- "${run[@]}"
perf report -i "$analysis_dir/perf.data" --stdio --no-children \
  > "$analysis_dir/report.txt"
perf report -i "$analysis_dir/perf.data" --stdio --no-demangle \
  > "$analysis_dir/symbols.txt"
```

先查函数和调用路径，再查指令。用 `symbols.txt` 中精确的 mangled name，保持符号模式一致：

```bash
hot_symbol='_Z...'
perf annotate -i "$analysis_dir/perf.data" --stdio --no-demangle \
  --symbol "$hot_symbol" > "$analysis_dir/annotate.txt"
objdump -drwC "$binary" > "$analysis_dir/disassembly.txt"
nm -S -C "$binary" > "$analysis_dir/symbol-sizes.txt"
```

目标在共享库时对相应库反汇编，并保留匹配的 ELF/build-id。优先保留符号与调试信息；需要另建诊断库时记录它与交付库的差异。annotation 为空先排查符号、DSO、build-id 和采样范围，不直接判定没采到热点。

采样频率和栈回溯有开销，检查 lost samples；profiler 运行时间不作为最终吞吐。按问题另选 cache、load/store、FP 向量事件，先用 `perf list` 和实际小组计数确认可用性，不把架构特定名称当作通用事件。

## 2. toplev：给硬件解释设边界

从较浅层级开始，底层计数有效后再扩到 L2。`--single-thread` 要求目标确为单线程，并按该 CPU 模型的要求保持同核 SMT sibling 空闲；`taskset` 只绑逻辑 CPU，不能保证这一点。先查可见拓扑与同核活动；VM 中若无法确认宿主侧条件，保留该限制，不把精确 TopDown 百分比作为确定归因。不能满足前提时选该 CPU 支持的其他模式或降低到可验证的 perf 计数。满足前提的可重复工作负载示例：

```bash
python3 "$pmu_tools/toplev.py" --single-thread --user \
  --no-multiplex -l1 -v --no-desc -x, \
  -o "$analysis_dir/topdown-l1.csv" \
  --perf-output "$analysis_dir/topdown-l1-raw.csv" -- "${run[@]}"
```

核对 raw 后，将 `-l1` 改为 `-l2`，使用新输出名。`--no-multiplex` 可能重复执行工作负载收集不同事件组；各轮须可比，不能把它当作单次完整同步观测。保留 stdout/stderr、原始事件、有效运行比例和工具版本。

- 全零 cycles、`<not counted>`、强 multiplex 或不合理百分比，均先判定指标无效；返回码成功、MUX=100% 单独都不充分。
- 若失败与事件组容量有关，检查底层分组并尝试更小的组。本次 VM 上 `--reserved-counters 1 --no-multiplex --single-thread --user -l2 -v` 产生了有效 raw；这是经验证的局部解法，不是所有机器的固定参数。
- 不直接展开所有深层节点。较浅层有效，不保证更深组可计数；保留失败 raw，停止使用失效层级。
- 比较比例时同时看总工作量与绝对计数。优化后 Core_Bound 占比上升，可能只是其他成本减少，不能据此声称绝对 core 成本增加。

## 3. 实际汇编/IR + LLVM-MCA：把类别变成机制

以匹配 perf build-id 的最终 ELF 热区为实际执行证据。从 `compile_commands.json` 或真实构建日志复用工作目录、编译器和全部有效 flags，生成诊断汇编及向量化报告；只改输出动作，不悄悄增加 native、fast-math 或 alignment。GCC 可增加 `-S -fverbose-asm -fopt-info-vec-all=...`；Clang 可用 `-Rpass=loop-vectorize -Rpass-missed=loop-vectorize`，需要 IR 时用 `-S -emit-llvm`。

启用 LTO 时，改成 `-S` 可能得到 LTO 数据/IR，或遗漏链接期内联与特化；诊断 `.s` 不能直接冒充最终热区。使用链接后的原生汇编，或将最终反汇编按工具语法重建，并核对模型输入对应的指令与依赖。跨编译器生成的 IR 是该编译器的诊断，不能当作原 GCC 二进制证据。以实际汇编验证 SIMD 宽度、FMA、标量余项、转换、拷贝、分支和 spill；pragma 存在不证明构建 flags 生效。IR 中存在 alloca 也不单独证明热路径有栈拷贝。

核对诊断汇编与最终热区后，从热点提取明确的一次循环迭代，保留依赖与必要指令，在可供分析的汇编副本中用注释界定：

```asm
# LLVM-MCA-BEGIN hot
# 此处放实际热点指令及必要标签，不放伪造的等价快路径
# LLVM-MCA-END hot
```

```bash
llvm-mca-19 -mcpu=skylake-avx512 -iterations=100 \
  -bottleneck-analysis -all-stats "$analysis_dir/loop.s" \
  > "$analysis_dir/mca.txt"
```

模型按实际 CPU 选择；`-mcpu` 选择模型，不会把输入 SSE 指令自动变成 AVX。比较同样工作量的 cycles、Block RThroughput、uops、端口压力与依赖停顿；需要时添加 timeline。总模拟 cycles/迭代数和 Block RThroughput 是不同指标。参见 [LLVM-MCA 文档](https://llvm.org/docs/CommandGuide/llvm-mca.html)。

嵌套循环不能只提取一遍内循环指令就声称是一次完整输出；显式展开时说明展开次数。静态工具不按真实分支概率执行整段控制流，初始化、边界或备用路径不应随意拼成一个会全部执行的基本块。模型不证明真实 cache miss、调度或完整应用速度。

## 4. 按未决问题选择补充工具

### llvm-exegesis：核对关键指令延迟/倒数吞吐

只有依赖链或模型数值值得核实时才做小范围微测，例如：

```bash
llvm-exegesis-19 --mode=latency --opcode-name=ADDSDrr \
  --benchmark-repeat-count=5 --min-instructions=10000 \
  > "$analysis_dir/exegesis-addsd.yaml"
```

需要倒数吞吐时核对当前版本 `--mode=inverse_throughput`。检查 YAML 的 `error`、生成 snippet 和目标 CPU；LLVM 内部 opcode 名称、权限与计数器支持均须实际验证。单条 add 延迟不能推出整个 dot 或应用的提速。参见 [llvm-exegesis 文档](https://llvm.org/docs/CommandGuide/llvm-exegesis.html)。

### Cachegrind：追踪指令数和访存来源

```bash
valgrind --tool=cachegrind --cache-sim=yes --branch-sim=yes \
  --cachegrind-out-file="$analysis_dir/cachegrind.out" "${bench[@]}"
cg_annotate --auto=no --threshold=0 "$analysis_dir/cachegrind.out" \
  > "$analysis_dir/cachegrind.txt"
```

看 Ir、Dr/Dw、D1/LL misses 及源码归属。确认所需 cache 列确实生成，程序完成且输出/状态仍正确；不使用 Valgrind wall time 评价速度。模拟 cache 结果用于定位工作量，不代替硬件 PMU。若独立解包运行，显式配置相应 `VALGRIND_LIB`；遇到 unsupported instruction、brk 或映射警告，核对产物后决定哪些结论仍有效，不把警告自动归为无害。

### uiCA / OSACA：交叉检查同一个热点

只在已有模型解释仍有疑问时使用，按模型支持范围选择架构。uiCA 需要可反汇编对象；OSACA 需要明确的汇编片段：

```bash
as "$analysis_dir/loop.s" -o "$analysis_dir/loop.o"
"$model_python" "$uica_root/uiCA.py" "$analysis_dir/loop.o" \
  -arch SKX > "$analysis_dir/uica.txt"
"$model_python" -m osaca --arch SKX --syntax ATT "$analysis_dir/loop.s" \
  > "$analysis_dir/osaca.txt"
```

本例 `loop.s` 应仅含待测循环、必要标签/常量及汇编器所需信息；MCA 注释不负责替 uiCA/OSACA 裁剪整份文件。不要为组装方便删掉真实 load、转换或收尾；标量内循环的展开和控制流限制同样适用。

核对 AT&T/Intel 语法、架构和未知指令，不能用 ignore-unknown 后的残缺结果证明收益。模型共享 cache 命中等假设，几种模型接近只能支持机制解释，不能按多数票取代同 ISA 的 A/B。uiCA setup 缺 setuptools 等依赖时只修工具环境，不改变生产构建。

## 把工具证据落到候选

每次输出一个可被实验否定的机制判断，例如“转换与点积争用执行资源”，再做隔离的小改动；不要把“端口忙”直接变成采用 SIMD、增加缓存或放宽数值语义的理由。每轮记录实际采样 → 指令证据 → 模型假设 → A/B 与反例结果。工具没有新信号或候选已被门禁否决时，停止追加模型和参数扫描。

## 比较脚手架也要核对

- C/C++ 混编时，仅找到或链接 C OpenMP target，不证明 C++ 热点带上了 `-fopenmp`；检查实际 TU 命令与汇编，使用不支持 OpenMP 的构建验证回退。
- 同一个 C++ 文件编译两份后一起链接，入口重命名不足以保证相互隔离：模板、weak/COMDAT 和静态表构造可能被合并。优先使用独立程序/库，或明确隔离相关符号并验证实际调用对象；不要盲目 localize weak symbols 导致 discarded-section 错误。
- 输出计数、phase/游标和状态的检查应独立于数值误差门禁；改变 reduction 顺序时，不能把放宽结构检查当作允许舍入差异。
