# System Design 101 来源与吸收边界

## 本页导航

1. 来源角色、快照和许可边界
2. 蒸馏方法
3. 四个 pattern 家族的来源映射
4. 案例索引怎样使用
5. 不吸收的默认规则
6. 材料局限

## 来源角色

`System Design 101` 为本技能补充具体系统结构模式、失效场景和演化案例。它不是新的设计哲学，也不改变来源优先级：

1. 《软件设计的哲学（第二版）》决定复杂性、模块深度、信息隐藏和性能测量尺度；
2. 《架构整洁之道》与《架构设计的本质》补充依赖、用例、系统边界和设计链；
3. `System Design 101` 只提供可以被上述尺度裁决的模式候选、反例和案例问题。

当来源发生张力时，模式必须降级为条件候选；不能以“业界常用”“生产级组件”或公司案例覆盖主书。

## 材料快照

- 仓库：`ByteByteGoHq/system-design-101`
- 快照：`b28380a4710c5ec9638ec037d4168e288f334cba`
- 提交日期：2025-04-04
- 本地材料：`data/guides/` 下 400 篇 Markdown
- 上游快照：<https://github.com/ByteByteGoHq/system-design-101/tree/b28380a4710c5ec9638ec037d4168e288f334cba>
- 许可证：仓库 `LICENSE.md` 声明 CC BY-NC-ND 4.0

本技能不复制上游图表和长段原文；只独立重述通用结构判断并保留来源索引。上游大量内容以远程图片为主，本次只将本地 Markdown 中可审计的正文作为规则证据。公司架构文章均视为二手、时间敏感快照，不能证明公司当前状态。

## 蒸馏方法

五个独立视角分别提取框架、原则、案例、反例和术语，再按以下门禁合并：

1. 能否从模式名还原真实压力、契约和知识所有者；
2. 是否给出结构不同的候选，而不是直接映射到一个组件；
3. 是否写明代价、失效方式、验证和退出条件；
4. 是否能与现有 11 个方法联合；
5. 是否避免把局部实现技巧升级为架构问题；
6. 是否不依赖特定测试仓库、公司规模或产品名称。

仅有模式名、工具清单、面试流程或远程图片而无正文条件的材料，没有提升为运行规则。

## 模式来源映射

路径均相对上游仓库。

### 结构与边界

| 主题 | 主要来源 |
|---|---|
| 模式目录与边界风格 | `data/guides/6-software-architectural-patterns-you-must-know.md`；`data/guides/top-9-architectural-patterns-for-data-and-communication-flow.md` |
| 微服务准入和反例 | `data/guides/is-microservice-architecture-the-silver-bullet.md`；`data/guides/9-best-practices-for-building-microservices.md` |
| 模块共置与通信成本 | `data/guides/amazon-prime-video-monitoring-service.md` |
| 服务粒度演化 | `data/guides/evolution-of-airbnb's-microservice.md`；`data/guides/airbnb-artchitectural-evolution.md` |
| Gateway、BFF 与联邦 | `data/guides/evolution-of-the-netflix-api-architecture.md`；`data/guides/graphql-adoption-patterns.md` |
| 仓库拓扑 | `data/guides/monorepo-vs.md`；`data/guides/how-tiktok-manages-a-200k-file-frontend-monorepo.md` |
| REST/GraphQL/RPC 与更新连接 | `data/guides/rest-api-vs-graphql.md`；`data/guides/shortlong-polling-sse-websocket.md` |
| 认证状态与授权政策 | `data/guides/cookies-vs-sessions-vs-jwt-vs-paseto.md`；`data/guides/how-do-we-design-a-permission-system.md` |

运行规则见 [结构与边界模式](patterns-structure-and-boundaries.md)。

### 通信与工作流

| 主题 | 主要来源 |
|---|---|
| 异步请求—回复、竞争消费者、Claim Check、优先队列 | `data/guides/top-6-cloud-messaging-patterns.md` |
| 队列到日志/分层存储的演化 | `data/guides/how-do-message-queue-architectures-evolve.md` |
| 编排与协同 | `data/guides/orchestration-vs-choreography-microservices.md` |
| 最终一致性与 Saga | `data/guides/top-eventual-consistency-patterns-you-must-know.md` |
| 消息交付语义 | `data/guides/delivery-semantics.md`；`data/guides/can-kafka-lose-messages.md` |
| 幂等与结果未知 | `data/guides/top-6-cases-to-apply-idempotency.md`；`data/guides/how-to-avoid-double-payment.md` |
| 重试 | `data/guides/how-do-we-retry-on-failures.md`；`data/guides/how-to-handle-web-request-error.md` |
| 更新通道 | `data/guides/polling-vs-webhooks.md`；`data/guides/shortlong-polling-sse-websocket.md` |
| Schema 演化 | `data/guides/smooth-data-migration-with-avro.md` |

运行规则见 [通信与工作流模式](patterns-communication-and-workflows.md)。

### 数据与一致性

| 主题 | 主要来源 |
|---|---|
| 工作负载驱动数据库选择 | `data/guides/choose-the-right-database-for-metric-collecting-system.md`；`data/guides/how-do-you-decide-which-type-of-database-to-use.md` |
| 缓存准入与同步策略 | `data/guides/things-to-consider-when-using-cache.md`；`data/guides/top-5-caching-strategies.md` |
| 缓存失效放大 | `data/guides/how-can-cache-systems-go-wrong.md` |
| 读副本 | `data/guides/read-replica-pattern.md`；`data/guides/how-to-implement-read-replica-pattern.md` |
| 分片、键和一致性哈希 | `data/guides/a-crash-course-in-database-sharding.md`；`data/guides/top-4-data-sharding-algorithms-explained.md`；`data/guides/consistent-hashing.md` |
| CAP 与正常态权衡 | `data/guides/cap-theorem-one-of-the-most-misunderstood-terms.md` |
| 状态、CQRS、Event Sourcing 与 CDC | `data/guides/how-do-we-manage-data.md`；`data/guides/how-do-we-incorporate-event-sourcing-into-the-systems.md`；`data/guides/change-data-capture-key-to-leverage-real-time-data.md` |
| 并发控制 | `data/guides/pessimistic-vs-optimistic-locking.md` |
| 唯一 ID | `data/guides/unique-id-generator.md`；`data/guides/explaining-5-unique-id-generators-in-distributed-systems.md` |
| 对账 | `data/guides/reconciliation-in-payment.md` |
| 存储抽象 | `data/guides/storage-systems-overview.md` |

运行规则见 [数据与一致性模式](patterns-data-and-consistency.md)。

### 韧性、伸缩与交付

| 主题 | 主要来源 |
|---|---|
| 韧性模式目录 | `data/guides/resiliency-patterns.md` |
| 高可用拓扑 | `data/guides/how-do-we-design-for-high-availability.md` |
| 故障探测 | `data/guides/how-do-we-detect-node-failures-in-distributed-systems.md` |
| 伸缩与容量 | `data/guides/a-crash-course-on-architectural-scalability.md`；`data/guides/how-to-scale-a-website-to-support-millions-of-users.md` |
| 并发与并行 | `data/guides/concurrency-is-not-parallelism.md` |
| 批处理与流处理 | `data/guides/10-system-design-tradeoffs-you-cannot-ignore.md` |
| 发布策略 | `data/guides/kubernetes-deployment-strategies.md`；`data/guides/how-to-deploy-services.md` |
| 灾备 | `data/guides/cloud-disaster-recovery-strategies.md` |
| 可观测信号 | `data/guides/logging-tracing-metrics.md` |

运行规则见 [韧性、伸缩与交付模式](patterns-resilience-scale-and-delivery.md)。

## 案例索引怎样使用

下表只提供可移植的提问，不提供可复制的技术选型：

| 案例材料 | 可提炼的问题 |
|---|---|
| `100x-postgres-scaling-at-figma.md` | 是否先使用更简单的容量手段，并且每一步由连接、表尺寸、Vacuum 或 IOPS 等具体证据触发？ |
| `how-discord-stores-trillions-of-messages.md` | 数据库迁移是否同时验证 p99、GC/compaction、热点和运维成本，而非只看吞吐？ |
| `amazon-prime-video-monitoring-service.md` | 逻辑组件是否被误当作必须独立进程；状态转换和大中间数据传输是否成为已测成本？ |
| `evolution-of-the-netflix-api-architecture.md` | 聚合规则应属于客户端、BFF、中央 Gateway 还是领域团队？ |
| `how-redis-architecture-evolve.md` | 每一层持久化、复制、选主、分片或多线程是否只回答一个已经出现的失败/瓶颈？ |
| `how-levelsfyi-scaled-to-millions-of-users-with-google-sheets.md` | 当前简单结构是否仍满足核心流程；升级触发器是什么？ |
| `the-one-line-change-that-reduced-clone-times-by-a-whopping-99-says-pinterest.md` | 架构迁移前，瓶颈是否只是错误工作集或工具配置？ |
| `4-ways-netflix-uses-caching-to-hold-user-attention.md` | 同一缓存技术承担的状态角色是否分别定义权威、可丢失性和重建？ |
| `mcdonald's-event-driven-architecture.md` | 事件驱动是否同时拥有 schema、SDK、权限、分片、修复与运维面？ |
| `10-principles-for-building-resilient-payment-systems-by-shopify.md` | 韧性是否由失败矩阵、幂等、对账、容量演练和事故责任共同形成，而非一个组件？ |

案例中的数字、公司拓扑和结果只用于理解材料原语境；在当前任务中必须重新取得事实。

## 明确不吸收为默认规则

- 大型或“生产级”系统必须有负载均衡、缓存、队列、搜索、服务发现、容器和 Kubernetes；
- 云原生意味着从单体迁移到微服务，或有状态组件天然是反模式；
- 一个服务只做一件事，并且每个服务必须有独立物理数据库；
- 微服务天然可扩展、容错或低耦合；
- 读多就缓存、慢查询就分片、要高可用就双活；
- 异步、发布订阅、协同或最终一致性天然比同步/编排/事务高级；
- Broker 的 exactly-once 等于最终业务副作用只发生一次；
- 所有 4xx 永不重试、所有 5xx 都可重试；
- 两个节点的可用性可以脱离独立故障和切换行为直接相乘；
- 热点键永不过期、所有服务无状态、所有读都走副本；
- CAP、数据库类别、协议名或架构模式名可以独立决定选型；
- 公司案例和“典型”延迟、超时、RTO/RPO 数字可直接移植。

## 已知材料局限

- 内容以视觉化和简化说明为目标，不是完整方法论；
- 多篇正文只罗列名称或组件，缺少准入、失败和退出；
- 部分术语混用，例如消息交付与业务处理效果、CQRS 与 Event Sourcing；
- 部分表述互相矛盾，例如一处把单体/有状态称为反模式，另一处又承认低延迟状态型系统不适合拆服务；
- 公司案例是二手摘要，可能省略关键约束和失败史；
- 工具、云服务和性能数字会过时；
- 远程图片不构成本技能可审计的规则来源。

若需要引用当前产品能力、公司现状或具体配置，必须另查一手、版本化资料；本页不能代替官方文档。
