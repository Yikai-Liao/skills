# clarity 来源与采用边界

本页供维护者核对规则来源、真实案例与版本。实际执行要求由 [技能主文件](../../clarity/SKILL.md) 及其参考维护；验证结果见 [测试说明](../../tests/clarity/test-results.md)。

真实来源的节选、中文概括与教学反例分别标明。仓库源码优先固定提交或标签；滚动页面可能变化。公开原文、行业建议与模型模拟不能相互替代为效果证据。

## 共同原则与既有技能

| 来源 | 采用与边界 |
|---|---|
| [International Plain Language Federation](https://www.iplfederation.org/plain-language/) | 读者找到、理解并使用所需信息；只读公开说明，未读取完整 ISO 24495-1，不声称标准认证 |
| [Google Technical Writing：Audience](https://developers.google.com/tech-writing/one/audience) | 按读者知识与任务补背景，不假定所有读者都是初学者 |
| jaal：[clarify-doc](https://github.com/jaal/claude-code-skills/blob/5d10ede31758d7d4127490de8e9d3fa2c774ff9a/skills/clarify-doc/SKILL.md) | 意图、概念与发现证据；未采用固定检查顺序和每次交付双份版本 |
| DocWriter：[plain-writing](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/skills/plain-writing/SKILL.md) | 必要背景、解释与稳定术语；未采用英语禁词、标点禁令或从句配额 |
| bholmesdev：[simplify](https://github.com/bholmesdev/skills/blob/44da67bd1896cdafced6f60573b62ae71d18ef2a/skills/simplify/SKILL.md) | 命名、概念与派生状态；未采用词源偏好、机械合并或自动删除兼容路径 |
| jesse-merhi：[reducing-cognitive-load](https://github.com/jesse-merhi/skills/blob/830a4dcd4938db687d759cc449be00456670fdc7/skills/reducing-cognitive-load/SKILL.md) | 准确名称、单位、保契约与有意义的拆分；没有把对话中更广的 schema/协议理论归给原文 |
| kenn-io：[code-simplifier](https://github.com/kenn-io/forge/blob/81e7b7eff2ba994c0c0750bc56f54659250ebd91/skills/code-simplifier/SKILL.md) | 保行为、守范围、反对过度内联；原文已反对只追求少行数，未将其误写成相反主张 |

用户提供的两份 ChatGPT 讨论用于明确需求；其中未独立核对的学术名词、中文 AI 句式频率和训练机制解释未作为事实采用。泛称 `technical-writing` 无法唯一定位，不指定任意同名仓库替代。DocWriter 的[模型 eval](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/evals/README.md)不证明本技能提高真人阅读速度。

## 文本关系与研究论文

对应 [文本写作](../../clarity/references/text-writing.md)。

| 来源 | 采用与边界 |
|---|---|
| [Google：Recognize ambiguous pronouns](https://developers.google.com/tech-writing/one/words#recognize_ambiguous_pronouns) | 原例中的认证能力可能来自 ID、权限或两者；中文候选是条件式教学改写，不代选事实。Google 页面使用 CC BY 4.0 |
| [RST：关系定义](https://www.sfu.ca/rst/01intro/definitions.html) | 核对 Contrast、Antithesis、Concession 的定义与示例；不混同传统修辞的同名术语，不按连接词直接判谬误 |
| [UNC Writing Center：Transitions](https://writingcenter.unc.edu/tips-and-tools/transitions/) | 已读完整正文；连接语表达具体关系，不能补救缺失的组织。运行时采用自主表述，未复制或改编该讲义的案例与表格 |
| [Silvennoinen：Contrastive negation and register](https://varieng.helsinki.fi/series/volumes/19/silvennoinen/) | 定向读取摘要、分类、方法、频率表与讨论。Table 3 的会话频率为每千词 1.30，报刊为 0.84；形式随语体变化，不能推出“人类日常很少用否定”或中文 AI 比较 |
| [Nordmeyer 与 Frank：The pragmatics of negation across contexts](https://langcog.stanford.edu/papers/NF-cogsci2015.pdf) | 完整读取六页；两项实验分析 92、184 名英语母语成人的情境合宜度判断。支持性情境提高真实否定句评分；运行时摘要是简化中文摘述，未复跑数据，也未推广成句式禁令 |
| [Mensh 与 Kording：Ten simple rules for structuring papers](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619) | 完整读取 2017 年 Editorial，DOI 10.1371/journal.pcbi.1005619，CC BY 4.0。采用贡献、摘要与证据链组织；CCC、单次出现和多人反馈不作为所有任务的硬要求 |

用户提供的[论文十条规则中文转载](https://zhuanlan.zhihu.com/p/696738723)只读取离线剪藏。原文 Rule 2 的 “Think like a designer” 是建议，剪藏连接方式容易反转这一含义；Rule 7 要求图标题表达结论、图注解释方法，不能据转载省去图注。未核验完整转载授权链或该文的全部下游引用。

“把有帮助抬成保证再否定”及连续段落反复纠偏的检查，是结合读者任务与保真要求形成的编辑判断，不称为上述论文已实验验证的规则。

## 软件指南、契约与架构

对应 [软件文档](../../clarity/references/software-documentation.md)。

### 实际文档案例

| 来源与版本 | 案例用途 |
|---|---|
| [Ruff README](https://github.com/astral-sh/ruff/blob/b2f4973cda296939ce5d0740287fd66e2af0d5e3/README.md) | 安装、lint 与格式化的任务分流；普通格式化会写回，禁止写回时仍需核对检查配置与选项 |
| [dbt README](https://github.com/dbt-labs/dbt-core/blob/13cd99c47deb5376929003a28883487cfe704de2/README.md) | 安装入门、理解项目、报告问题与贡献的不同入口；未将版本迁移或 beta 条件泛化到所有版本 |
| [Firecracker Getting Started](https://github.com/firecracker-microvm/firecracker/blob/dcfc69b625d0ffd9c65efd81fe2eff445012881a/docs/getting-started.md) | Linux/KVM、设备访问和演示/生产隔离边界；运行时为中文摘要，未启动虚拟机 |
| Django 5.2：[get() 文档](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#get)、[固定源码](https://github.com/django/django/blob/9e7cc2b628fe8fd3895986af9b7fc9525034c1b0/docs/ref/models/querysets.txt#L2141-L2176) | 唯一、零个、多个匹配对象的结果及异常归属；未安装 Django 或执行查询 |
| [KEP-753 固定提交](https://github.com/kubernetes/enhancements/blob/2f57ef9064946203f5b0e0f012a56a29159c85b3/keps/sig-node/753-sidecar-containers/README.md) | Goals/Non-Goals、Proposal、Test Plan 与 Graduation Criteria；阶段安排是历史提案材料，不将旧 feature gate 条款当成[当前 sidecar](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)回退指令 |

### C4 与开发计划

C4 定义以官方[总览](https://c4model.com/diagrams)、[container 抽象](https://c4model.com/abstractions/container)、[系统上下文](https://c4model.com/diagrams/system-context)、[容器图](https://c4model.com/diagrams/container)、[动态视图](https://c4model.com/diagrams/dynamic)与[部署视图](https://c4model.com/diagrams/deployment)为准。实际查看了 [SystemContext.png](https://c4model.com/images/examples/SystemContext.png) 和 [Containers.png](https://c4model.com/images/examples/Containers.png)：Simon Brown 的虚构 Internet Banking System，CC BY 4.0。运行时是简化文字摘录，不是真实银行方案。C1/C2 的推荐不等于每次局部任务必须重画两图。

[OpenAI ExecPlans](https://developers.openai.com/cookbook/articles/codex_exec_plans)提供复杂长任务的自包含、里程碑与恢复约定。项目采用该协议时遵守完整格式；普通开发计划只借鉴所需信息，不自动创建 PLANS.md 或继承提交、发布权限。

以下二手来源已读取正文，用于补充文档检查角度，不作为效果证据或新流程授权：

- [Bool](https://bool.dev/blog/detail/architecture-documentation-best-practice)与[Docsie](https://www.docsie.io/blog/glossary/system-architecture-documentation/)：架构、决定与维护；C4 定义回查官方，不采用营销数字。
- [Codacy](https://blog.codacy.com/code-documentation)：意图、接口、依赖、示例与失效文档维护。
- [daily.dev](https://daily.dev/blog/7-best-practices-for-planning-developer-documentation/)与[Sonat](https://sonat.com/blog/documentation-plan/)：主要讨论文档规划；不能据此证明通用软件实施流程，不复制示例 KPI、工期或管理模板。
- [Zemith 原中文路径](https://www.zemith.com/zh/blogs/best-practices-for-documentation)实际为英文正文，canonical 为[英文地址](https://zemith.com/blogs/best-practices-for-documentation)；采用任务组织和示例辅助，不采用产品推荐或固定审查周期。

### 候选索引与迁移入口

[readme-best-practices 模板](https://github.com/jehna/readme-best-practices/blob/ef2d30ae0ec30e6f18642c4386f9c8d205182c68/README-default.md)、[awesome-readme](https://github.com/matiassingers/awesome-readme/blob/18195faec9697b21bb8086cfc8059c617b615b3d/readme.md)、[awesome-oss-docs](https://github.com/saintmalik/awesome-oss-docs/blob/1347d8f56fb467642a731127556d103e4f30983b/README.md)用于发现缺口与候选，已采用案例另读实际文件。[OpenSSF 指南](https://github.com/ossf/wg-best-practices-os-developers/blob/76ea1b82be806e6ceacd2ecfe22e9f774d8f825e/docs/Concise-Guide-for-Developing-More-Secure-Software.md)仅采用可发现的安全报告入口等文档边界。

Neovim [旧 README](https://github.com/neovim/neovim/blob/master/src/nvim/README.md)只剩迁移提示。对应正文入口为 [dev_arch.txt](https://github.com/neovim/neovim/blob/master/runtime/doc/dev_arch.txt)（布局、状态机与阅读顺序）、[dev_tools.txt](https://github.com/neovim/neovim/blob/master/runtime/doc/dev_tools.txt)（开发调试工具）和 [dev.txt](https://github.com/neovim/neovim/blob/master/runtime/doc/dev.txt)（开发、文档与错误约定）；这些是已核对用途的滚动入口，未作为运行时架构案例。

## 代码结构、注释与诊断

对应 [代码可理解性](../../clarity/references/code-readability.md)。

### 结构与真实源码

- Fowler 的 [Extract Variable](https://refactoring.com/catalog/extractVariable.html) 与 [Split Phase](https://refactoring.com/catalog/splitPhase.html)：只读公开目录示例。运行时价格公式为教学改写，非真实项目重构历史。
- [Google Go Style Guide](https://google.github.io/styleguide/go/guide.html#clarity)与[代码审查指导](https://google.github.io/eng-practices/review/reviewer/looking-for.html)：按调用与维护任务看名称、复杂度和注释，不将完整审查流程加入所有写作任务。
- Linux 的[函数](https://www.kernel.org/doc/html/latest/process/coding-style.html#functions)与[集中退出](https://www.kernel.org/doc/html/latest/process/coding-style.html#centralized-exiting-of-functions)：职责与共享清理，不采用行数或单出口配额。
- CPython v3.13.0：[compiler_mod](https://github.com/python/cpython/blob/60403a5409ff2c3f3b07dd2ca91a7a3e096839c7/Python/compile.c#L1721-L1737)，连同 [compiler_codegen](https://github.com/python/cpython/blob/60403a5409ff2c3f3b07dd2ca91a7a3e096839c7/Python/compile.c#L1682-L1710) 和 [optimize_and_assemble](https://github.com/python/cpython/blob/60403a5409ff2c3f3b07dd2ca91a7a3e096839c7/Python/compile.c#L7684-L7701) 核对。运行时保留实际函数，展示阶段与作用域退出；[许可](https://github.com/python/cpython/blob/60403a5409ff2c3f3b07dd2ca91a7a3e096839c7/LICENSE)。
- Go go1.24.0：[protoAtLeast](https://github.com/golang/go/blob/3901409b5d0fb7c85a3e6730a59943cc93b2835c/src/net/http/transfer.go#L455-L457)保留完整紧凑比较，仅调整缩进；同文件 [readTransfer](https://github.com/golang/go/blob/3901409b5d0fb7c85a3e6730a59943cc93b2835c/src/net/http/transfer.go#L491-L606)辅助理解阶段分区；[许可](https://github.com/golang/go/blob/3901409b5d0fb7c85a3e6730a59943cc93b2835c/LICENSE)。
- Go go1.23.0：[IndexRune](https://github.com/golang/go/blob/go1.23.0/src/strings/strings.go#L122-L143)的 API 注释在 122—125 行；字节偏移由实现与调用核对，不把单位说明错误归给原注释。
- CPython v3.13.3：[list_resize](https://github.com/python/cpython/blob/v3.13.3/Objects/listobject.c#L113-L145)解释预留容量与连续追加成本。中文注释为机制概括，增长公式不是所有分配路径，未测量性能。

### 注释文章及读取方式

[Boot.dev](https://www.boot.dev/blog/computer-science/code-comments)、[Mirai Solutions](https://mirai-solutions.ch/py-techguides/best-practices/documentation-and-comments.html) 和 [Tobenna Oduah](https://tobennaoduah.substack.com/p/best-practices-for-commenting-your-code-well-c2114fd52714)已由研究代理读取；前两篇另经维护核对。采用契约、docstring 渠道、非显然理由与更新要求；不采用 Boot.dev 的不完整清洗片段作为安全 regex 实现，不把不返回值的 Go 函数一律判错，也不强制私有函数使用完整模板。

下列两页在线抓取为 403，内容核对使用用户提供的完整 Markdown 剪藏；这不表示在线访问已恢复：

- [Real Python：comments](https://realpython.com/ref/best-practices/comments/)：Leodanis Pozo Ramos，审阅者 Brenda Weleschuk、Bartosz Zaczyński。局部原因与公开 docstring 分工支持现有边界。
- [Stack Exchange：method/class comments](https://softwareengineering.stackexchange.com/questions/96882/what-information-should-a-good-method-class-comment-contain)：区分 fresskoma 的问题与六个回答，不称为共识。Aaronaught 将所有详细解释外移、提交前删除所有 TODO 的要求未采用；Gnawme 的 Dewhurst 引文仅通过回答读取。元数据中的 S.Lott 没有可辨识的回答正文，不为其归纳立场。

### 诊断信息

- Rust 官方书[所有权章节](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)与[固定 E0382 输出](https://github.com/rust-lang/book/blob/1500248d8f230566e4ec9f27fcbb8fe9e2898ab1/listings/ch04-understanding-ownership/no-listing-04-cant-use-after-move/output.txt)：两个短节选匹配该输出，未实际运行 Rust 编译器；克隆建议的性能条件保留。
- Google [错误信息](https://developers.google.com/tech-writing/error-messages)、[原因](https://developers.google.com/tech-writing/error-messages/identify-the-cause)、[修复建议](https://developers.google.com/tech-writing/error-messages/show-fix)、[后端约定](https://developers.google.com/tech-writing/error-messages/back-end)：CPU 配额为教学改写，额外保留跨区域权限条件，非真实故障数据；页面使用 CC BY 4.0。
- [CLIG Errors](https://clig.dev/#errors)：采用有用上下文和诊断入口；原文确有“最重要信息放在输出末尾”的建议，未推广为通用顺序，也未把 chmod 例子当成通用修复。

## 长篇与语言适配

对应 [长篇写作](../../clarity/references/long-form-writing.md)与[语言适配](../../clarity/references/language-adaptation.md)。

- Django 5.2 的[文档入口](https://docs.djangoproject.com/en/5.2/#how-the-documentation-is-organized)和[固定目录源码](https://github.com/django/django/blob/9e7cc2b628fe8fd3895986af9b7fc9525034c1b0/docs/index.txt#L49-L69)：真实的教程、概念、参考与任务入口，运行时表格为中文概括；不要求小手册凑齐四类。
- IPCC AR6 [Summary for Policymakers](https://www.ipcc.ch/report/ar6/syr/summary-for-policymakers/)，2023 年 A.1/A.1.1：运行时只摘述 2011—2020 相对 1850—1900 高约 1.1°C 的含义，未核验底层气候数据。
- [W3C Date formats](https://www.w3.org/International/questions/qa-date-format)：先确认日期身份，再适配显示；不从页面语言推断 `03/04/02` 的年月日，不采用该页旧平台实现代码。
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.txt) 第 1、3、5 节与 [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.txt) 第 2 节：运行时为中文释义，保留规范强度、大写适用条件及不用大写词仍可能有规范要求的边界。

## 指令与审查证据

对应 [指令写作](../../clarity/references/instruction-writing.md)与[审查验证](../../clarity/references/review-and-validation.md)。

- [OpenAI：Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)：触发范围、按需上下文、决策边界与完成条件；模型特定能力判断未纳入通用规则。
- Anthropic PDF skill 固定提交：[主文件](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/pdf/SKILL.md#L7-L11)、[目录](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/pdf)、[forms.md](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/pdf/forms.md)。主文件的大写引用与实际小写文件不符，大写地址曾返回 404。运行时用自主文字概括分流并校正名称，未复制专有许可下的流程或脚本。
- GDS 的[观察便签](https://userresearch.blog.gov.uk/2014/10/29/anatomy-of-a-good-sticky-note/)、[图片](https://userresearch.blog.gov.uk/wp-content/uploads/sites/102/2014/10/the-perfect-sticky-note-620x417.jpg)及[分析研究过程](https://www.gov.uk/service-manual/user-research/analyse-a-research-session)：已查看原图，`5` 是参与者编号。运行时保留原话，错误人数和界面原因属于教学反例；未取得完整参与者记录。
- [Sonar Cognitive Complexity](https://www.sonarsource.com/resources/cognitive-complexity/)只读取资源落地页，未读取白皮书，不采用评分公式或将其用于证明真人理解效果。

## 内容核对覆盖

来源实质审计曾覆盖 67 项原始 URL/片段：60 项有相关主体内容、5 项为索引、1 项为白皮书落地页、1 项只剩迁移提示。原始清单中的重复片段和临时行号定位记录不作为当前导航；本页保留实际采用的入口及上述重要校准。

后续九个软件文档来源分别取得七份在线正文和两份离线剪藏；对比/语境另核对四项来源，论文结构另核对一项出版社原文。这些是分批内容核对，不是对本页所有滚动 URL 未来可用性的保证，也不涵盖 awesome 索引的全部下游。
