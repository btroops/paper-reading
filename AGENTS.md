# AGENTS.md

> **开工前必读**：`STATUS.md` 记录仓库当前进度与下一步。开工先读，收工更新，规则见第 9 节。
> **笔记怎么写**：`WWH.md` 是阅读模型与笔记结构标准（Why → What → How → Ideas），第 5 节只给骨架。

本仓库用于存放论文原文与精读笔记。论文种类繁多，**不按研究方向或论文类型划分目录**；分类信息写在笔记的 `tags` 里。

## 0. 硬性约束（优先于任何风格偏好）

- **只在仓库内操作**：所有读取、写入、执行都在仓库根目录内完成。不读写仓库外的路径（家目录、系统临时目录、上级目录等），不 `cd` 出仓库，不修改 shell / git / 包管理器等全局配置。
- **禁止绝对路径**：仓库内任何文件的内容——笔记、文档、脚本、配置、示例命令、图片链接——都不得出现本机绝对路径（以斜杠开头的用户目录、盘符路径等）。一律使用相对仓库根目录的路径，例如 `notes/jiang2026-jev-mem.md`、`notes/assets/jiang2026-jev-mem/fig-1.png`。本仓库会发布到 GitHub，clone 者的路径必然不同。
- **原文只读**：`papers/` 下的 PDF 与补充材料只读，不改名、不压缩、不覆盖、不删除。
- **不臆造**：论文没写的内容不要补。实验数字、作者、年份、venue 必须能在原文中找到；不确定就写 `TODO:` 或 `?`，并说明缺口在哪。
- **来源外链用 URL**：引用论文、代码、数据集时用公开链接（如 `https://arxiv.org/abs/...`），不要写本地路径。
- **Python 只用 uv**：任何解释器、依赖、脚本执行都遵守第 3 节，不走 `pip` / `conda` / 系统 Python。

## 1. 目录结构

```text
.
├── AGENTS.md            # 本文件
├── WWH.md               # 文献阅读模型：笔记结构标准（Why/What/How/Ideas）
├── STATUS.md            # 跨会话进度（所有 agent 必读）
├── README.md            # 论文索引（唯一入口，需手工维护）
├── pyproject.toml       # uv 项目定义（提交）
├── uv.lock              # 依赖锁（提交）
├── .python-version      # 固定 Python 版本（提交）
├── papers/
│   └── <paper-id>/
│       ├── paper.pdf
│       └── paper.txt    # 本地生成，不提交
├── notes/
│   ├── <paper-id>.md    # 一篇论文一份笔记
│   └── assets/
│       └── <paper-id>/  # 该笔记的图表截图
└── tools/               # 可复用脚本，如 pdf_extract.py
```

- 论文与笔记一一对应，**不建立 `nlp/`、`cv/`、`survey/` 之类的分类目录**。
- 仓库根目录若存在散落的 PDF（历史遗留），在首次精读时移动到 `papers/<paper-id>/paper.pdf`，不要复制。
- 笔记内引用图片用相对路径：`![fig-1](assets/<paper-id>/fig-1.png)`。
- **不提交**：`.venv/`、`__pycache__/`、`*.pyc`、`papers/*/paper.txt`，均已写入 `.gitignore`。

## 2. 命名约定

`paper-id` 是论文的唯一标识，也是目录名与笔记名。**必须让人一眼看出这是哪篇论文**，因此统一采用「第一作者姓 + 年份 + 短标题」，不把 arXiv 编号当目录名：

```text
<第一作者姓><年份>-<短标题>
jiang2026-jev-mem
vaswani2017-attention
```

- **第一作者姓**：小写 ASCII，非拉丁姓名转写，如 `zhang`、`müller` 写作 `muller`。
- **年份**：论文首次公开的年份（arXiv 取 v1 提交年），四位数字，不带分隔符。
- **短标题**：2–4 个实词，小写 kebab-case；去掉 `A/An/The/On/Towards` 这类虚词；专有名词与方法名保留原拼写，如 `jev-mem`、`rag`。
- **唯一性**：同作者同年同关键词时补一个区分词，仍冲突再加 `-2`、`-3`，如 `jiang2026-magma` 与 `jiang2026-hage`。
- **arXiv 编号不进名字**：写在笔记 front matter 的 `arxiv` 字段与 `README.md` 索引的 `arxiv` 列，保证可回溯但不污染目录名。
- 同一论文的不同版本视为同一篇：id 不变，版本差异写在笔记里；确需区分时用 `title` 与 `arxiv` 字段说明，不改目录名。
- 已存在的编号目录（以 arXiv 编号作目录名）**立即改名**，用 `git mv` 保留历史，不在仓库里长期共存两种命名；改名后同步笔记里的图片路径与 `README.md` 索引。

## 3. Python 环境与 PDF 解析

- **工具链只允许 uv**：初始化、装包、锁依赖、运行脚本全部通过 `uv`。禁止 `pip`、`pip3`、`python -m pip`、`conda`、`poetry`、`pipenv`、`--user` 安装、系统级安装，也不要手工 `source .venv/bin/activate` 后裸跑 `python`。
- **Python 版本：3.12**，由 uv 管理，`.python-version` 固定为 `3.12`。选择理由：本机系统 Python 只有 3.8（过旧），3.12 对 PDF 解析库的兼容性最好且 uv 已有现成解释器。变更版本需在提交信息中说明原因。
- **首次初始化**（仓库根，只做一次）：

  ```bash
  uv init --bare --vcs none --no-readme --python 3.12
  uv add pymupdf
  ```

- **执行脚本**统一用 `uv run <script.py>`，例如 `uv run tools/pdf_extract.py papers/<paper-id>/paper.pdf`。
- **依赖按需添加**：默认只装 `pymupdf`（文本、版面、图片提取）；需要表格解析时再加 `pdfplumber`；不要预装 OCR、深度学习等重型依赖。依赖变动必须同时更新并提交 `pyproject.toml` 与 `uv.lock`。
- **不使用外部命令**：不依赖 `pdftotext`、系统 OCR 等仓库外工具，避免不同机器结果不一致。
- uv 的下载缓存与解释器目录位于仓库外，属于工具自身机制，不算越界；但虚拟环境、锁文件、脚本输出等项目产物必须留在仓库内。

首次解析前创建 `tools/pdf_extract.py`（之后复用，不要每篇重写）：

```python
import sys
from pathlib import Path

import pymupdf


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: uv run tools/pdf_extract.py papers/<paper-id>/paper.pdf")
    src = Path(sys.argv[1])
    doc = pymupdf.open(src)
    target = src.with_suffix(".txt")
    target.write_text(
        "\n\n".join(page.get_text("text") for page in doc), encoding="utf-8"
    )
    print(f"{target} | {doc.page_count} pages")


if __name__ == "__main__":
    main()
```

需要图表时用 `page.get_pixmap(clip=rect, dpi=200).save(path)` 裁剪，输出到 `notes/assets/<paper-id>/`；PDF 本身保持原样。

## 4. 阅读工作流

1. **定位论文**：确定 `paper-id`，确认 `papers/<paper-id>/paper.pdf` 存在；缺失时先补原文，不要凭记忆写笔记。
2. **提取内容**：运行 `uv run tools/pdf_extract.py papers/<paper-id>/paper.pdf` 生成 `paper.txt` 供分块阅读；重要图表按第 3 节方式截图。
3. **写笔记**：按 `WWH.md` 的四段结构 + 第 5 节骨架输出到 `notes/<paper-id>.md`。阅读顺序为 Abstract → Conclusion → Introduction → 方法/实验 → Ideas；读不懂的段落如实标注，不要用常识填坑。
4. **推 Ideas**：回到 Why/What/How 找缺口，按 `WWH.md` 第 7 节的三步推导写创新点，每条必须带最小验证与失败条件。
5. **更新索引**：在 `README.md` 的表格中新增或更新一行。`README.md` 不存在时创建。
6. **收尾**：删除本次产生的中间文件；自检第 7 节清单。

## 5. 笔记模板

结构与判定标准见 `WWH.md`，本节只给骨架；两者冲突时以 `WWH.md` 为准。

```markdown
---
title: "<论文标题>"
authors: ["<作者1>", "<作者2>"]
year: 2026
venue: "<会议/期刊/arXiv>"
arxiv: "https://arxiv.org/abs/<id>"   # 非 arXiv 论文留空
tags: ["agent-memory", "retrieval"]
status: reading   # reading | done | shelved
model: WWH-v1     # 遵循的阅读模型版本，见 WWH.md
---

# <论文标题>

## Why
要解决什么问题、为什么现在必须解决、现有方法在机制层面差在哪。取材 Introduction。

## What
### TL;DR
三句话内说清：解决什么问题、怎么做、结论是什么。

### 结论清单
按「新认识 / 新方法 / 新结论」分组，每条带证据锚点，标注 `[宣称]` 或 `[已验证]`。

## How
判型（试验 / 数值 / 理论 / 系统算法 / 实证基准 / 综述）→ 核心机制（输入→决策→状态变化→输出）→ 关键公式 → 证据强度（端到端 / 消融 / 单例）→ 开销与边界。
公式用 LaTeX；图用 `assets/<paper-id>/xxx.png` 引用。

## Ideas
### 不足
作者承认的局限 + 我发现的矛盾 + 未覆盖的场景 + 方法与评估的错配，逐条归因到数据 / 方法 / 评估 / 系统。

### 创新点
每条四要素：主张 / 与原文关系（增量·正交·反驳·扩展）/ 最小验证 / 失败条件。

## 相关工作
与本仓库已有笔记的异同，用相对链接互引，如 `[vaswani2017-attention](vaswani2017-attention.md)`；仓库内无同主题笔记时写论文自身的定位。

## 可复现
数据、算力、代码链接、关键超参。无法复现之处直接写明。
```

- `tags` 用英文小写 kebab-case，便于后续 `grep` 检索；不追求受控词表。
- 笔记默认中文书写，术语、指标、方法名保留英文原文。
- 论文页面引用格式：`§3.2`、`Fig. 4`、`Table 2`，不要写 PDF 页码路径。

## 6. README 索引

维护一张按 `paper-id` 倒序的表格，只增不删：

```markdown
| paper-id | 标题 | 年份 | arxiv | tags | status |
| --- | --- | --- | --- | --- | --- |
| [<paper-id>](notes/<paper-id>.md) | <标题> | <年份> | <arxiv-id> | tag-a, tag-b | reading |
```

- `paper-id` 列直接显示可读名字，不写编号；arXiv 编号单独一列，非 arXiv 论文留空。这样目录名给人看，编号给检索用。

## 7. 提交前自检

- [ ] 笔记的 front matter 字段完整（含 `model`），链接可解析。
- [ ] 四段齐全且顺序为 Why → What → How → Ideas；`What` 的结论标注了 `[宣称]` / `[已验证]`。
- [ ] `Ideas` 每条四要素齐全，且能追溯到前面某条不足。
- [ ] 所有图片路径为相对路径，且文件真实存在。
- [ ] `README.md` 索引已包含该论文。
- [ ] 仓库内没有绝对路径：
      `grep -rnE '/(home|Users)' --include='*.md' .` 应无输出。
- [ ] 未修改、未删除 `papers/` 下的原始 PDF。
- [ ] 依赖有变动时，`pyproject.toml` 与 `uv.lock` 已同步提交。
- [ ] 未提交 `.venv/`、`__pycache__/`、`*.pyc`、`paper.txt`。
- [ ] 提交已按第 8 节拆分：原文、笔记、索引各自独立，无无关改动夹带。
- [ ] `STATUS.md` 已更新，并以 `docs(status): ...` 单独提交。

## 8. 提交规范

格式：`<type>(<scope>): <简述>`。沿用 Conventional Commits，并增加 `paper`、`notes` 两个类型。

| type | 用途 | scope 示例 |
| --- | --- | --- |
| `chore` | 仓库脚手架、规则、忽略文件 | `repo` |
| `paper` | 论文原文与补充材料归档 | `jiang2026-jev-mem` |
| `notes` | 阅读笔记与图表资源 | `jiang2026-jev-mem` |
| `docs` | README 索引、状态记录、说明文档 | `index` / `status` |
| `build` | Python 环境与依赖 | `deps` |
| `fix` | 修正笔记中的事实、链接或数字错误 | `jiang2026-jev-mem` |

**粒度：一个提交只做一件事。**

- 一篇论文至少拆成三个提交，且按此顺序：
  1. `paper(<paper-id>): 归档 <标题> 原文`
  2. `notes(<paper-id>): <一句话结论>`
  3. `docs(index): 收录 <paper-id>`
- 不同论文的改动不得混在同一提交。
- 规则、依赖、内容三者分开：改 `AGENTS.md` 用 `chore`，改 `WWH.md` 用 `docs(model)`，改 `pyproject.toml` / `uv.lock` 用 `build`。
- 增量修改单独提交：补充分析用 `notes(<id>): 补充 xxx`，纠错用 `fix(<id>): 修正 xxx`，不要追加到旧提交。
- 重命名、格式化、批量整理等无关改动，不得夹带在内容提交里。

**写法：**

- 简述用中文，动词开头，不超过 50 字，结尾不加句号。
- 需要解释原因时，空行后写正文，每行不超过 72 字符。
- 一次提交的 diff 要能用一句话概括；做不到就继续拆。

**暂存与检查：**

- 禁止 `git add .` / `git add -A`，只 `git add <明确路径>`。
- 提交前用 `git diff --staged` 确认没有无关文件。
- 不 `--amend` 已推送的提交，不 `push --force`。

## 9. 会话交接（所有 agent 必读）

`STATUS.md` 是跨 agent、跨会话的唯一进度来源，只记录"现在做到哪了"，不重复规则与笔记内容。

- **开工**：先读 `STATUS.md` 再动手；与 `AGENTS.md` 冲突时以 `AGENTS.md` 为准，并顺手修正 `STATUS.md`。
- **收工**：会话结束前必须更新，至少覆盖：本次做了什么、当前进度、下一步、阻塞项。
- **只写事实**：已完成的事写结果（含提交 hash）；未完成写 `TODO` 并注明依赖；不写未经证实的推测。
- **控制长度**：保留当前快照 + 最近几次会话；更早的内容压缩成一行或删除，避免无限膨胀。
- **提交**：单独提交，格式 `docs(status): <一句话>`，不与论文内容混在同一提交。

## 10. 指令优先级

用户当次的明确指令优先于本文件的风格约定；但第 0 节的硬性约束不可绕过。若用户指令与之冲突，先说明冲突点，再执行。

`WWH.md` 与第 5 节冲突时，以 `WWH.md` 为准；它属于笔记结构标准，不属于风格偏好，也不得绕过第 0 节。
