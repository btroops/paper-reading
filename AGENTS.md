# AGENTS.md

本仓库用于存放论文原文与精读笔记。论文种类繁多，**不按研究方向或论文类型划分目录**；分类信息写在笔记的 `tags` 里。

## 0. 硬性约束（优先于任何风格偏好）

- **只在仓库内操作**：所有读取、写入、执行都在仓库根目录内完成。不读写仓库外的路径（家目录、系统临时目录、上级目录等），不 `cd` 出仓库，不修改 shell / git / 包管理器等全局配置。
- **禁止绝对路径**：仓库内任何文件的内容——笔记、文档、脚本、配置、示例命令、图片链接——都不得出现本机绝对路径（以斜杠开头的用户目录、盘符路径等）。一律使用相对仓库根目录的路径，例如 `notes/2609.23986v1.md`、`notes/assets/2609.23986v1/fig-1.png`。本仓库会发布到 GitHub，clone 者的路径必然不同。
- **原文只读**：`papers/` 下的 PDF 与补充材料只读，不改名、不压缩、不覆盖、不删除。
- **不臆造**：论文没写的内容不要补。实验数字、作者、年份、venue 必须能在原文中找到；不确定就写 `TODO:` 或 `?`，并说明缺口在哪。
- **来源外链用 URL**：引用论文、代码、数据集时用公开链接（如 `https://arxiv.org/abs/...`），不要写本地路径。
- **Python 只用 uv**：任何解释器、依赖、脚本执行都遵守第 3 节，不走 `pip` / `conda` / 系统 Python。

## 1. 目录结构

```text
.
├── AGENTS.md            # 本文件
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

`paper-id` 是论文的唯一标识：

- arXiv 论文：用编号，保留版本号，与 PDF 文件名一致，如 `2609.23986v1`。
- 非 arXiv 论文：`第一作者姓+年份+关键词`，全小写 kebab-case，如 `vaswani2017-attention`。
- 同一论文的不同版本视为同一篇，id 用最新已读版本，版本差异写在笔记里。

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
3. **写笔记**：按第 5 节模板输出到 `notes/<paper-id>.md`。先写 TL;DR，再补细节；读不懂的段落如实标注，不要用常识填坑。
4. **更新索引**：在 `README.md` 的表格中新增或更新一行。`README.md` 不存在时创建。
5. **收尾**：删除本次产生的中间文件；自检第 7 节清单。

## 5. 笔记模板

```markdown
---
title: "<论文标题>"
authors: ["<作者1>", "<作者2>"]
year: 2026
venue: "<会议/期刊/arXiv>"
arxiv: "https://arxiv.org/abs/<id>"   # 非 arXiv 论文留空
tags: ["agent-memory", "retrieval"]
status: reading   # reading | done | shelved
---

# <论文标题>

## TL;DR
三句话内说清：解决什么问题、怎么做、结论是什么。

## 问题与动机
作者要解决的痛点，以及对现有方法的批评。

## 方法
核心机制、关键公式、必要图示。公式用 LaTeX；图用 `assets/<paper-id>/xxx.png` 引用。

## 关键实验
只记录能支撑结论的设置与数字，标明数据集、指标、对比基线。

## 局限与疑问
作者承认的局限 + 自己的质疑。未验证的推测写成 `TODO:`。

## 与相关工作的关系
与本仓库已有笔记的异同，用相对链接互引，如 `[vaswani2017-attention](vaswani2017-attention.md)`。

## 可复现要点
数据、算力、代码链接、关键超参。无法复现之处直接写明。
```

- `tags` 用英文小写 kebab-case，便于后续 `grep` 检索；不追求受控词表。
- 笔记默认中文书写，术语、指标、方法名保留英文原文。
- 论文页面引用格式：`§3.2`、`Fig. 4`、`Table 2`，不要写 PDF 页码路径。

## 6. README 索引

维护一张按 `paper-id` 倒序的表格，只增不删：

```markdown
| paper-id | 标题 | 年份 | tags | status |
| --- | --- | --- | --- | --- |
| [<paper-id>](notes/<paper-id>.md) | <标题> | <年份> | tag-a, tag-b | reading |
```

## 7. 提交前自检

- [ ] 笔记的 front matter 字段完整，链接可解析。
- [ ] 所有图片路径为相对路径，且文件真实存在。
- [ ] `README.md` 索引已包含该论文。
- [ ] 仓库内没有绝对路径：
      `grep -rnE '/(home|Users)' --include='*.md' .` 应无输出。
- [ ] 未修改、未删除 `papers/` 下的原始 PDF。
- [ ] 依赖有变动时，`pyproject.toml` 与 `uv.lock` 已同步提交。
- [ ] 未提交 `.venv/`、`__pycache__/`、`*.pyc`、`paper.txt`。
- [ ] 提交已按第 8 节拆分：原文、笔记、索引各自独立，无无关改动夹带。

## 8. 提交规范

格式：`<type>(<scope>): <简述>`。沿用 Conventional Commits，并增加 `paper`、`notes` 两个类型。

| type | 用途 | scope 示例 |
| --- | --- | --- |
| `chore` | 仓库脚手架、规则、忽略文件 | `repo` |
| `paper` | 论文原文与补充材料归档 | `2609.23986v1` |
| `notes` | 阅读笔记与图表资源 | `2609.23986v1` |
| `docs` | README 索引、说明文档 | `index` |
| `build` | Python 环境与依赖 | `deps` |
| `fix` | 修正笔记中的事实、链接或数字错误 | `2609.23986v1` |

**粒度：一个提交只做一件事。**

- 一篇论文至少拆成三个提交，且按此顺序：
  1. `paper(<paper-id>): 归档 <标题> 原文`
  2. `notes(<paper-id>): <一句话结论>`
  3. `docs(index): 收录 <paper-id>`
- 不同论文的改动不得混在同一提交。
- 规则、依赖、内容三者分开：改 `AGENTS.md` 用 `chore`，改 `pyproject.toml` / `uv.lock` 用 `build`。
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

## 9. 指令优先级

用户当次的明确指令优先于本文件的风格约定；但第 0 节的硬性约束不可绕过。若用户指令与之冲突，先说明冲突点，再执行。
