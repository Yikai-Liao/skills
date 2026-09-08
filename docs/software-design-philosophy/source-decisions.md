# 来源与裁决

仓库维护记录，不随 skill 安装，也不是运行时前置流程。以下依据是本仓库重构前提交 `1f3d992` 的来源裁决和测试记录；本轮未重新核验原书、外部材料快照或历史测试原始执行日志。原有逐章书摘、问答全文和旧测试报告可从 Git 历史恢复。

## 来源角色

- John Ousterhout《软件设计的哲学（第二版）》：复杂性、信息隐藏、深模块、候选比较和性能判断的主要视角。
- Robert C. Martin《架构整洁之道》与《架构设计的本质》：补充变化轴、依赖方向、系统边界与生命周期责任；不把层级、用例或技术标签当边界结论。
- 用户提供的 Linux 文件系统设计讨论：补充共同资源不变量、完整工作流与可重新汇入的高级能力。
- `ByteByteGoHq/system-design-101`：旧记录使用快照 `b28380a4710c5ec9638ec037d4168e288f334cba` 提取结构候选。现仅保留与边界、状态及失败语义有关的判断，不保留公司案例、产品/协议百科、容量数字或上游图文。

这些来源是设计视角与历史依据，不覆盖当前用户明确要求。具体有效规则只在下列运行时文件维护；本页不再复制一套执行摘要或要求重新裁决已确定的偏好。

## 个人取舍的处理

| 旧记录 | 保留的目的 / 本轮处理 | 当前权威位置 |
|---|---|---|
| C01 测试与设计 | 保留不默认用 TDD 生成架构、按风险验证；删除每步完成标准与统一测试配额 | [SKILL.md](../../software-design-philosophy/SKILL.md) |
| C02 有限接口 | 保留共同不变量、完整工作流、长尾归属与逃逸重新汇入；合并重复表格 | [深模块与接口](../../software-design-philosophy/references/design-deep-modules.md) |
| C03 未来选项 | 保留当前简洁性和有证据、难逆变化的窄接缝 | [SKILL.md](../../software-design-philosophy/SKILL.md) |
| C04/C06 用例与指标 | 保留知识/变化证据，不按用例、类数或局部依赖指标自动重构 | [模块与知识边界](../../software-design-philosophy/references/design-module-boundaries.md) |
| C05 重要性与性能 | 保留先查接口缺口、必要性能入口与首版主流程优先；性能背景不扩展用户目标 | [性能约束下的设计](../../software-design-philosophy/references/design-measured-critical-paths.md)及入口的任务范围规则 |
| C07 实现继承 | 保留个人明确排斥多基类实现继承的取舍，不推广为语言事实 | [模块与知识边界](../../software-design-philosophy/references/design-module-boundaries.md) |
| C08 调试面 | 保留显式需求、易于 Agent 使用及生产隔离；将“每次深模块设计主动询问”缩窄到实际设计该能力时补足必要范围 | [深模块与接口](../../software-design-philosophy/references/design-deep-modules.md) |
| C09 架构分类 | 保留相对评价范围、结构机制与局部修复的区别；删除强制双轨等级与报告模板 | [架构审计](../../software-design-philosophy/references/audit-software-architecture.md) |
| C10–C12 模式补充 | 保留压力、权威、失败和代价；将四类百科合并为条件性系统契约，不保留全量加载要求 | [系统边界与失败契约](../../software-design-philosophy/references/design-system-boundaries.md) |

这些个人偏好有仓库中的明确答复记录，不能仅因模型可能自行推导而删除；它们不需要每次重新询问。当前重构任务已明确要求重验范围过宽的旧规则，因此调整了 C08 的询问范围。

## 历史失败保留到哪里

旧测试记录指出三类行为错误：用严重度替代架构类别、让性能背景接管交付、方法互斥导致遗漏。它们分别由审计准入、入口任务范围和按需联合保护。

旧版本还记录“先发现问题再加载判据”的召回盲区，后续用全读 11 个方法及四个模式家族修补。本轮把具体发现问题、证据与反证放入紧凑的审计 reference，再按需进入设计细节，保留发现能力的目的，删除全量阅读机制。新结构的实际召回效果仍需行为评估，文件校验不能证明它。
