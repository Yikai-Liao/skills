# Agent 技能库

用于研究写作、软件设计和清晰表达的可复用技能，通过 [skills CLI](https://skills.sh/) 安装。

## 选择技能

| 技能 | 适用任务 |
|---|---|
| [`survey-md`](survey-md/SKILL.md) | 起草、修订或审查有来源依据的学术综述与文献回顾。 |
| [`software-design-philosophy`](software-design-philosophy/SKILL.md) | 分析软件复杂性，设计模块、接口、系统边界与演化方案。 |
| [`clarity`](clarity/SKILL.md) | 起草、改写或审查文稿、软件文档与指令，改善代码可理解性，并保留语义与行为。 |

`clarity` 覆盖书籍、报告、README、需求、API 规格、C4 架构文档和开发计划，也指导文档路径与标题组织、函数/类/变量命名。不用于纯格式修改或没有阅读问题的代码实现。技能说明使用中文，交付物遵循用户指定的语言。

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
