# 代码行为夹具与隔离执行

本目录是维护输入，不随 skill 安装。代码均为自拟小样例，不是上游项目摘录或推荐重构答案。唯一裁判脚本是上级目录的 [check_behavior.py](../check_behavior.py)，仅用 Python 标准库，不负责模型调用或可读性评分。

## 给执行者什么

每题使用新工作目录，只复制下表指定输入、当前题面的 `prompt`，以及本次安装条件下的技能运行时文件。执行者不能读取用例 JSON、本文、裁判脚本、来源记录、研究中的候选改写、历史评分或其他执行者答案。不要把整个仓库作为工作目录交给执行者后仅要求它忽略 expected；由维护者准备最小输入，并记录实际可访问范围和读取证据。

| 用例 ID | 执行者输入 | 产物与裁判 |
|---|---|---|
| `code-new-multistep-implementation` | `catalog_new.py` 复制为 `catalog.py`；`catalog_contract.md` | `catalog.py`；`catalog` 检查 |
| `code-extract-single-use-stage` | `catalog.py`；`catalog_contract.md` | `catalog.py`；`catalog` 检查 |
| `code-flatten-error-priority` | `workflow.py` | `workflow.py`；`workflow` 检查 |
| `code-preserve-cohesive-parser` | `escaped_fields.py` | 原样保留或修改后的文件及简短判断；`parser` 检查 |
| `inline-unreused-helper`（复用原题） | `inline_helper.py` 和原题 | 修改后的文件；`inline` 检查 |
| `code-rust-lock-state-safety` | `lock_state.rs` | 只审查的答复；本轮无 Rust 可执行裁判 |

新实现题不能看到已有 `catalog.py`。`catalog_new.py` 是未实现起点，其行为检查预期失败；不能把它计入已完成代码。原有 `inline-with-local-concepts`、`code-async-semantics`、`code-coherent-function`、`implementation-only`、`format-only` 和只审查题继续用原题，不另造同义用例。代码题必须提交实际源码，不能以重述原则代替。

## 维护者运行行为检查

在仓库根目录运行；最后一个参数也可换成执行者实际交付文件的绝对路径。裁判在执行结束后运行，不向执行者提供断言或自动修正候选。

```sh
python -B tests/clarity/check_behavior.py catalog tests/clarity/fixtures/catalog.py
python -B tests/clarity/check_behavior.py workflow tests/clarity/fixtures/workflow.py
python -B tests/clarity/check_behavior.py parser tests/clarity/fixtures/escaped_fields.py
python -B tests/clarity/check_behavior.py inline tests/clarity/fixtures/inline_helper.py
```

这些命令检查输入夹具自身的 14 个测试方法，包含多个子例，不是 14 个独立模型样本。应另检查裁判能拒绝逐行提交、交换校验优先级、遗漏尾部转义错误、缺键默认为空等已知坏变体。通过只证明覆盖到的行为保持；没有自动断言函数数量、helper 名或长度。首次写入、阶段职责、状态追踪与跳转是否更清楚，由不知条件标签的读者查看真实产物。

Rust 输入用于审查锁作用域、两字段恢复与析构顺序。本轮环境没有 `rustc` 或 `cargo`，不把文本审查计为编译或运行。未来实际执行需记录精确工具链、edition 和 panic 配置，验证成功、返回 Err、unwind 的状态恢复和释放顺序；普通压力测试不等于穷尽并发证明，unwind 也不证明 abort 清理。

## 安装与效果证据分开

- 分别只复制 `clarity/`、只复制 `software-design-philosophy/`，检查各自全部运行时相对链接均在安装目录内、必要参考可读。来源与测试目录不可成为运行依赖。
- clarity 独立条件执行实际局部代码任务；design 独立条件回答内部阶段/不变量问题，不能要求安装另一技能。联合条件使用同一契约核对两套规则是否相容，不把局部整理自动升级为架构任务。
- 只给 description 的选择题测试触发意图；宿主实际发现和自然触发需另有运行证据。显式要求使用某 skill 只支持内容路径诊断。
- 如开展新旧配对比较，预先固定任务、两组技能快照、完整模型 ID/推理强度、宿主、权限、起点、预算及重复次数；随机交错运行，保留失败和未触发样本。判分前核对裁判哈希，不允许执行者修改断言。
- 分别报告静态有效、夹具自检、模型产物契约、真实读者理解和后续修改结果。保留功能失败总量；不把仅通过的漂亮产物或模型自评当作总体效果。未进行配对、真人阅读或递进修改时直接记未运行。
