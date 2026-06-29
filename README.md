# codex-skill-builder

把你的重复工作，封装成一个 Codex 一看就会用的 skill。

不是“再写一段更长的提示词”。这套工具的差异点是：**触发时机 + 工作流骨架 + 文件记忆 + 安全边界 + 可验证交付**。

## 三件套（MVP）

```text
Need Snapshot     先问少量关键问题，不陷入无尽访谈
Skill Blueprint   把想法拆成 SKILL.md / references / scripts / examples
Validate & Ship   生成预览版，校验结构，准备发布
```

后续可扩展：skill-review（评审已有 skill）、doc-to-skill（把 README/API/CLI 文档转成 skill）、package-skill（打包发布）。

## 你适合用它，如果你经常说

- “我有方案，但不知道怎么高效地让 Codex 替我执行。”
- “我每次都要让 Codex 按同一套流程做事。”
- “我有 README / API 文档 / 脚本，想让 Codex 稳定复用。”
- “我做了个 skill，但不知道触发描述、目录结构、安全边界对不对。”

## 它怎么工作

```text
粗糙想法 / 文档 / 脚本 / 清单
        ↓
Need Snapshot：确认输入、输出、禁区、成功标准
        ↓
Skill Blueprint：决定要不要 references / scripts / assets
        ↓
Workspace Preview：先生成预览，不直接污染全局 skill
        ↓
Validation：检查 SKILL.md、frontmatter、命名、结构
```

## 安装

```text
https://github.com/hey-zeyu/codex-skill-builder/tree/main/skills/codex-skill-builder
```

安装后重启 Codex。

## 用法

```text
Use codex-skill-builder. I want to turn my release checklist into a reusable Codex skill.
```

```text
Use codex-skill-builder. Convert this CLI README into a safe Codex skill.
```

```text
Use codex-skill-builder. Review this skill folder for trigger quality, structure, and safety.
```

更多例子：`examples/prompts.md`

## 设计原则

**Skill 不是提示词，是工作流容器。**

一个好 skill 应该回答五件事：

- 什么时候触发？
- 用户会给什么输入？
- Codex 应该按什么步骤做？
- 哪些知识应该放进文件，而不是塞进上下文？
- 哪些动作必须先确认？

## 进度记忆（文件，不靠模型记忆）

```text
SKILL.md                 主流程和触发逻辑
references/             长规则、方法论、示例
scripts/                可重复执行的确定性操作
examples/               真实触发语和 before/after
quick_validate.py       发布前结构校验
```

## 为什么不是直接问 Codex？

因为临场提示词会漂。

今天写得好，明天可能忘一步；这个会话知道，下个会话又要重讲。skill 的价值就是把“我会怎么做”沉淀成文件，让 Codex 下次继续按这套方式工作。

## 验证

```powershell
python .\skills\codex-skill-builder\scripts\quick_validate.py .\skills\codex-skill-builder
```

## 一句话传播

```text
I made a Codex skill that turns messy workflows, docs, scripts, and checklists into reusable Codex skills.
```

## License

MIT. See [LICENSE](LICENSE).
