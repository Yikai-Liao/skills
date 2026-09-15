# clarity 验证结果与使用限制

本页汇总与当前技能有关的验证证据。[测试用例](test-prompts.json)保存 55 个场景的输入与预期；来源和案例版本见 [来源记录](../../docs/clarity/sources.md)。

## 当前结论

- 最近一次 fresh-context Luna 全文件语义审查覆盖主文件、代理配置与七份参考，未发现实质规则冲突。
- 该次实际生成 12 项回答，审查者自评全部通过；维护者复核为 **11 pass、1 partial、0 fail**。
- 此后的文件改名与维护目录整理没有增加运行时规则。保真示例增加了对应小标题，通用 spec 状态要求移到 API 例子之前；路径与结构单独核对。
- 发布前另一次 fresh-context Luna 只读复核认可目录职责、参考命名、标题层级和证据压缩；指出根 README 的维护表未交代 `survey-md` 缺少独立维护材料，已补明范围。该次没有执行新的模型用例。

模型审查运行 ID：`8930676b-041a-4135-ae15-ab58c2dd5e91`。这是原文件名版本的审查记录；原始回复保留在执行会话中，本页记录有效结论和偏差，不复制逐轮对话。

## 已执行的结构检查

检查对象为 `clarity/`、`docs/clarity/`、`tests/clarity/` 和根 README：

- 九份运行时文件、七份参考，主文件路由与实际名称一致；运行时不依赖来源或测试记录。
- Frontmatter 名称与目录匹配；代理默认提示包含 `$clarity`；README 有安装和维护入口。
- 55 个用例 ID 唯一，均含输入、类型和预期；旧参考文件名已同步替换。
- 本地链接目标及使用到的标题锚点有效；Markdown 围栏配对，运行时无行尾空白。
- 目录整理保留既有来源的采用边界、案例版本与署名；删除临时来源清单、原始报告及重复状态汇总。
- `git diff --check` 通过。

这些检查不等于安装测试或真实运行环境的自动路由验证。

## 模型回答覆盖与偏差

| 场景 | 结果 |
|---|---|
| `compatible-not-opposed`：日志与测试的互补职责 | pass |
| `claim-task-match`：帮助理解与保证系统可靠性不同 | pass |
| `retain-grounded-correction`：保留有依据的日期更正 | pass |
| `retain-literary-contrast`：保留文学重心转移 | pass |
| `retain-consequential-limit`：保留样本与因果限制 | pass |
| `paper-abstract-scope`：论文摘要的证据与正文范围 | partial |
| `paper-structure-proportional`：CCC、回顾与方法的适用边界 | pass |
| `c4-levels`：系统、容器与部署副本分开 | pass |
| `execplan-scope`：评估协议适用性并完成局部改写 | pass |
| `api-docstring-contract`：工具可见性及调用契约 | pass |
| `plan-subject-not-editorial`：保留实施状态与理由 | pass |
| `code-only-validation`：只交付授权的代码改写 | pass |

`paper-abstract-scope` 的摘要末句为：“不能据此提出全面禁用否定句的结论。”给定研究考察语境与合宜度，没有讨论禁用政策；回答把提示中的防错要求带进了正文。现有正文与语境规则已覆盖这个问题，不为单次执行偏差追加同义规则，也未重写原回答后宣称原样通过。

这些回答出自预读 skill、维护材料与 expected 的同一审查上下文。55 是用例定义总数，不是本轮全量行为通过数；不同轮次的回答不合并为一次独立试验。

## 代码案例的直接核对

| 检查 | 结果与范围 |
|---|---|
| Node.js：异步包装与直接返回同步抛错 | 两项断言通过：async 返回 rejected Promise，普通包装可同步抛错 |
| Python：价格公式命名前后 | 12,288 个有限数值组合严格相等，另有四个边界场景符合预期；不覆盖自定义数值类型、非有限值或有副作用读取 |
| CPython `compiler_mod`、Go `protoAtLeast` | 分别按逐字、忽略空白方式与来源固定提交匹配；未构建原项目 |
| Go `IndexRune` 两个调用 | 本地 `go1.27.1-X:nodwarf5 linux/amd64`、`GOTOOLCHAIN=local` 返回字节偏移 3 和未找到 -1；不冒充来源 go1.23.0 全套测试 |
| Python docstring 与普通注释 | `inspect.getdoc` 能读取前者，不能读取后者；示例函数结果相同，未运行 Sphinx |
| Rust 诊断节选 | 两段文本与固定版本输出一致；未运行 Rust 编译器 |

上述实验针对相应案例编写时的版本；本次文件整理未改变代码围栏，也未重新运行这些语言实验。没有从有限测试推出所有输入等价或可读性效果。

## 尚未验证

- 自动选择技能、按需加载参考及跨会话稳定性。
- 全量 55 用例的独立行为试跑、无 skill 对照与跨模型比较。
- 真人阅读速度、理解正确率、满意度及母语者审校。
- 全部引用项目的构建、生产行为或性能。

后续改动应选择与风险有关的用例。静态一致、某次模型回答符合预期和人类效果分别记录，不能相互替代。
