# 论文精读

论文原文归档在 `papers/<paper-id>/`，精读笔记在 `notes/<paper-id>.md`。分类信息写在笔记的 `tags` 里，不建分类目录。

所有笔记遵循 [`WWH.md`](WWH.md) 阅读模型：**Why → What → How → Ideas**。每篇笔记的 front matter 用 `model:` 记录所依据的模型版本，方便日后按版本演进回填。

## 索引

按 `paper-id` 倒序排列。

| paper-id | 标题 | 年份 | arxiv | tags | status |
| --- | --- | --- | --- | --- | --- |
| [jiang2026-jev-mem](notes/jiang2026-jev-mem.md) | Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents | 2026 | [2609.23986](https://arxiv.org/abs/2609.23986) | agent-memory, memory-control, multi-relational-graph, adaptive-retrieval, efficiency, locomo | done |

## 工作流

见 `AGENTS.md`；当前进度见 `STATUS.md`。解析 PDF：

```bash
uv run tools/pdf_extract.py papers/<paper-id>/paper.pdf
```
