# 代码表达与可预测性

本页处理源码命名、结构、注释、docstring 与报错；独立手册和契约见[软件文档](software-documentation.md)。表达改进不代替设计决策或正确性证明。

## 保留本次任务要求的语义

首次编写表达既定需求；获准破坏性迭代可改名称、接口和结构；保行为重构保持约定的可观察行为；功能修改只改变获准范围。项目早期不自动授权破坏性变更，已有实现也不自动要求永久兼容。开发顺序、测试、兼容、状态管理和校验政策沿用任务与项目约定。

沿用有效的领域词汇、库能力和语言惯例。签名、名称与必要说明共同交代调用所需的输入、输出、条件、副作用、失败与资源责任，不给简单函数套文档模板。

## 定位具体阅读阻力

只追踪与当前问题有关的关系。跨阶段诊断可沿“入口 → 参数 → 状态 → 分支 → 副作用 → 结果 → 修改影响”阅读；局部改名不必记录整条调用链。

重点找名称与行为不符、单位或所有权不明、状态同步规则隐藏、分支依赖远处调用顺序、无意义转发拆散规则，以及密集表达式掩盖求值或错误传播。稳定契约能隐藏实现，文件数和跳转数本身不构成问题。

## 在定义与调用处看名称

| 对象 | 应说明什么 |
|---|---|
| 函数、方法 | 动作或所求结果，如 `reserve_stock`；不以 `get` 隐藏删除、扣款等副作用 |
| 类型、接口 | 对象、职责或能力，如 `Invoice`、`RetryPolicy`、Go `Reader`；不按 `Manager` 等后缀直接判错 |
| 变量、参数 | 角色、形状和必要单位，如 `subtotal`、`timeout_seconds`；已有单位类型时无需重复 |

包名、接收者和局部上下文已表达的信息不必重复。短作用域中明确的 `i`、`src`、`dst` 可保留；长期使用的 `data`、`tmp` 若需回查，应补角色。沿用 Python、Go、.NET 等各自的命名与导出惯例，不强推一种风格。

布尔名称让分支读作明确判断，准确的否定状态仍可保留。`is_`、`has_` 不保证无副作用；名称也无需塞进完整协议。

**实际命名：** Go go1.23.0 的 `io.Reader` 与 `io.ReadCloser` 区分能力，`io.Copy(dst Writer, src Reader)` 用参数和类型表达方向；关闭责任和成功返回 `nil` 而非 `EOF` 仍靠契约说明。CPython v3.13.0 的 `PurePath` 不访问文件系统，`Path` 提供可执行系统调用的方法，具体是否 I/O 看所用方法。

改名核对定义、调用、闭包与动态引用，区分同名符号。公共参数、JSON 键、数据库字段、反射名、CLI 和导入路径按既定兼容范围处理；保留语言要求的特殊拼写。例如协议键 `timeout_ms` 不动，内部可命名 `timeout_seconds = payload["timeout_ms"] / 1000`，原有舍入、溢出与缺省语义也须保留。

## 显露概念，不拆碎规则

- 用局部变量命名小计、折扣等有意义的结果，不用 `part1` 增加解码层。
- 将需一起理解或修改的规则聚合，让解析、领域计算和输出等阶段传递明确数据。
- 复用处理或隔离多步完整职责时，可提取有清楚契约的函数；不为凑短函数拆开同一不变量。
- 无清理工作的前置失败可早返回，共享资源可集中清理；保持错误优先级、清理路径和锁范围。
- 完整的布尔判断、查表与惯用法可紧凑保留；不要按代码外形相似合并不同知识或规则。

选择能直接显露概念或减少必要追踪的最小改动；不以换行、helper 数量为收益，也不要求每次交付另写结构报告。澄清状态名称与更新关系不授权删除状态、缓存或同步机制。

### 内联小 helper，不压平概念

本次涉及的一两行私有取值、计算或转发 helper，既无现有复用也无明确复用计划时，默认内联；“也许以后有用”不算计划。仅为命名一步计算时，用局部变量。不要内联已有深模块而扩大调用者需掌握的细节。

例如 `payload` 是普通字典，下列 helper 只有一个调用者，无动态引用或复用计划：

```python
def _get_items(payload):
    return payload["items"]

def item_names(payload):
    return [item["name"] for item in _get_items(payload)]
```

可改为：

```python
def item_names(payload):
    items = payload["items"]
    return [item["name"] for item in items]
```

### 命名计算中的概念

调整运费而不改商品折扣时，下式迫使读者从运算反解各项费用：

```python
return (
    unit_price * quantity
    - max(quantity - discount_after, 0) * unit_price * discount_rate
    + min(unit_price * quantity * shipping_rate, shipping_cap)
)
```

参数为普通数值，读取与计算无副作用时，可以命名局部结果，不新增函数：

```python
subtotal = unit_price * quantity
discounted_units = max(quantity - discount_after, 0)
discount = discounted_units * unit_price * discount_rate
shipping = min(subtotal * shipping_rate, shipping_cap)
return subtotal - discount + shipping
```

运费仍按折扣前小计计算。若是 getter、惰性或有副作用的读取，求值次数和时机也须保留。

### 用职责与资源生命周期划阶段

CPython 的模块编译入口用真实职责而非 `step1()` 区分阶段，并共享作用域退出路径：

```c
static PyCodeObject *
compiler_mod(struct compiler *c, mod_ty mod)
{
    PyCodeObject *co = NULL;
    int addNone = mod->kind != Expression_kind;
    if (compiler_enter_anonymous_scope(c, mod) < 0) {
        return NULL;
    }
    if (compiler_codegen(c, mod) < 0) {
        goto finally;
    }
    co = optimize_and_assemble(c, addNone);
finally:
    compiler_exit_scope(c);
    return co;
}
```

进入作用域失败直接返回；进入成功后，代码生成或组装即使失败也退出作用域。具体算法留在阶段内部，入口保留协作与生命周期。

### 保留完整的紧凑判断

Go 的版本比较共同表达一条规则，无需拆成三个 helper：

```go
func (t *transferReader) protoAtLeast(m, n int) bool {
    return t.ProtoMajor > m || (t.ProtoMajor == m && t.ProtoMinor >= n)
}
```

若本次涉及的这种小 helper 没有复用或明确计划，按前述规则将整个判断内联，需要命名时用局部布尔变量。同一错误处置下的简单校验可以合并，复杂流程仍显露阶段。

## 源码注释与 API 文档注释

注释说明局部代码无法表达的原因、契约、单位、算法依据和约束，主动保留 bug 与性能取舍的维护信息。API 注释同时说明行为与失败语义，不限于 why；Python docstring 等留在文档工具与 `help()` 能识别的位置。

签名、示例、说明与行为一致，不猜责任归属，不翻译机器标识符。旧实现为何改、收益与代价可以保留，删除聊天流水、编辑计划和空泛自评；私有函数无需统一注释模板。

**调用契约：** Go `strings.IndexRune` 搜索 Unicode 码点，未找到返回 `-1`；结果为字节偏移，`utf8.RuneError` 的特殊处理仍按 API 契约。只写“返回字符位置”会丢失这些信息。

```go
strings.IndexRune("中国", '国') // 3：字节偏移，不是字符序号。
strings.IndexRune("中国", '美') // -1：未找到。
```

### Bug 与性能修复

在关键代码旁说明必要的触发条件、旧方案为何失效、当前修复及防止回退的约束。例如已采用幂等键去重的支付接口：

```ts
// 超时不代表支付失败，服务端可能已完成扣款。
// 重试必须复用原幂等键；生成新键可能导致再次扣款。
```

优化说明节省的工作、适用负载和代价。因缓存、批处理或预分配而更难读时，留下原因，不为表面简洁撤销有效优化。CPython `list_resize` 解释预留容量与追加成本，可概括为：

```c
/* 按扩容策略预留额外容量，减少连续追加时的反复分配与可能的搬移。
   用一定的空闲容量换取长序列追加的摊销效率，而非每次都按当前长度精确分配。 */
```

这比“已经优化，请勿修改”更能支持维护。收益数字须有实测及负载、环境或 benchmark 依据；只有机制分析时，不编性能数值。长复现与报告链接到真实记录，局部仍保留防误改所需的解释，行为变化时同步更新。

## 报错与诊断信息

报错让读者识别失败并决定下一步，改措辞不授权改错误机制。

- 指出操作、对象、已知原因或违反的条件，区分确定、候选与未知。
- 必要时交代尚未执行、部分完成或状态未知；超时不证明失败或回滚。
- 下一步有事实和权限依据，不编按钮、参数或地址，不默认提权、关闭校验或重试副作用操作；无明确修复时给诊断或求助入口。
- 保留位置、字段和关联编号，不泄露凭据或无关敏感信息；用户消息与维护诊断可分层。
- 错误码、异常类型、退出状态、通道、结构化字段及机器依赖的消息原文，遵循既定兼容约定。

**定位与条件：** Rust 示例中 `let s2 = s1;` 移走 `String` 后又使用 `s1`，诊断连接移动与再次使用两处位置，并解释类型不实现 `Copy`：

```text
error[E0382]: borrow of moved value: `s1`
```

建议同时保留成本条件：

```text
help: consider cloning the value if the performance cost is acceptable
```

**数量与约束：** 已知请求量和配额时，比“资源不足”更有用的消息是：

> 请求的 2.0 CPUs 超出 us-central-1 区域的 1.0 CPUs 配额。可申请提高该区域配额；若其他区域有足够配额，且任务允许跨区域执行，也可选择其他区域。

跨区域方案须符合数据驻留、资源依赖和权限；系统未提供的数量不猜。

## 跨语言语义

遵循各语言惯用法：Go 显式错误、Python 推导式、Rust 所有权与匹配、SQL 集合操作不必统一成命令式步骤。

惰性求值、同步/异步异常、空值与真值、溢出、Unicode、求值顺序、资源释放和并发均属于行为。例如将 `async function load() { return await api.load(); }` 改成普通函数直接返回 `api.load()`，可能改变同步抛错的暴露方式，不能因少了包装就接受。
