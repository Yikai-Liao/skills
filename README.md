# Agent 技能库

用于研究写作、软件设计和清晰表达的可复用技能，通过 [skills CLI](https://skills.sh/) 安装。

## 选择技能

| 技能 | 适用任务 |
|---|---|
| [`survey-md`](survey-md/SKILL.md) | 起草、修订或审查有来源依据的学术综述与文献回顾。 |
| [`software-design-philosophy`](software-design-philosophy/SKILL.md) | 分析软件复杂性，设计模块、接口、系统边界与演化方案。 |
| [`clarity`](clarity/SKILL.md) | 面向用户解释和汇报，起草、改写或审查持久化文本；按需支持设计讨论、决定记录与代码可理解性改进。 |

`clarity` 同时用于会话中的答疑、进展与调研汇报，以及书籍、报告、README、需求、API 规格和架构文档等持久化文本。需要讨论设计、记录决定或接续实施反馈时，按需读取设计讨论参考；普通回复和润色无需增加这些步骤。工具执行、验证和审批权限沿用任务与项目要求。技能说明使用中文，交付物遵循用户指定的语言。

## 安装

按名称安装一个技能：

```bash
npx skills add Yikai-Liao/skills --skill clarity
```

将 `clarity` 替换为上表中的其他技能名称，即可安装对应技能。

也可以改为安装本仓库的全部技能：

```bash
npx skills add Yikai-Liao/skills --all
```

## 维护入口

各技能的顶层目录保存可安装内容，包括 `SKILL.md` 及运行时元数据、参考、脚本或资源。仅供开发维护使用的材料放在 `docs/<skill>/` 和 `tests/<skill>/`，不随技能安装。

下表列出已有的独立维护材料；`survey-md` 尚未设立对应的维护文档与测试目录，其运行时参考和脚本见[技能主文件](survey-md/SKILL.md)。

| 技能 | 来源与维护说明 | 验证材料 |
|---|---|---|
| `clarity` | [维护指南](docs/clarity/README.md) | [验证结果](tests/clarity/test-results.md) · [测试用例](tests/clarity/test-prompts.json) |
| `software-design-philosophy` | [来源与裁决](docs/software-design-philosophy/source-decisions.md) | [验证结果](tests/software-design-philosophy/test-results.md) · [测试用例](tests/software-design-philosophy/test-prompts.json) |
