# 工作流模式参考

用于选择 skill 的内部结构。

## 顺序工作流

适合明确步骤的任务，例如：视频转写、PDF 表单填写、数据清洗。

```markdown
## Workflow

1. Validate input.
2. Prepare working files.
3. Run the helper script.
4. Inspect output.
5. Fix and repeat if validation fails.
```

中文说明：

```markdown
## 工作流

1. 检查输入。
2. 准备工作文件。
3. 运行辅助脚本。
4. 检查输出。
5. 如果验证失败，修复后重试。
```

## 条件工作流

适合根据输入类型走不同路径的任务。

```markdown
If the user provides a local file, process it directly.
If the user provides a URL, confirm it is allowed and fetch metadata first.
If the input is missing, ask for the minimal required information.
```

中文说明：

```markdown
如果用户给本地文件，直接处理。
如果用户给 URL，先确认是否允许处理并读取元信息。
如果缺少输入，只问最少必要信息。
```

## 验证反馈循环

适合质量敏感任务。

```markdown
1. Generate or edit files.
2. Run validation.
3. If validation fails, read the specific error.
4. Patch the smallest necessary change.
5. Validate again.
6. Report what passed and what remains risky.
```

中文说明：

```markdown
1. 生成或编辑文件。
2. 运行验证。
3. 如果验证失败，读取具体错误。
4. 做最小必要修复。
5. 再次验证。
6. 汇报通过项和残留风险。
```

## README/API/CLI 转 Skill

```markdown
1. Identify tool type.
2. Extract user-facing tasks.
3. Write the shortest reliable workflow into SKILL.md.
4. Move detailed commands and errors into references/.
5. Add safety boundaries.
6. Add realistic prompt examples.
7. Validate the generated skill.
```

中文说明：

```markdown
1. 判断工具类型。
2. 提取用户真正会用的任务。
3. 把最短可靠流程写进 SKILL.md。
4. 把详细命令和报错放进 references/。
5. 补安全边界。
6. 增加真实触发示例。
7. 验证生成的 skill。
```
