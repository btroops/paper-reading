# 仓库状态

> 所有 agent 开工前先读本文件，收工前更新。规则见 `AGENTS.md` 第 9 节。

## 当前快照

- 分支：`main`
- 最近内容提交：`93f8f22 paper(2609.23986v1): 归档论文原文`（提交信息里的旧 id 是历史记录，不回改）
- 已归档论文：1 篇（`jiang2026-jev-mem`，arXiv 2609.23986v1）
- 已精读论文：1 篇（`jiang2026-jev-mem`）
- 阅读模型：`WWH-v2`（`WWH.md`），含结构与表达标准
- 命名规则：`<第一作者姓><年份>-<短标题>`，arXiv 编号只写在 front matter 与 README 索引
- Python 环境：uv + Python 3.12，已装 `pymupdf`（`pyproject.toml` / `uv.lock` 已生成，未提交）
- 进行中：无

## 最近会话

### 2026-10-29 WWH 升到 v2：补表达标准

- 起因：笔记的 Why 读两三遍仍看不懂，说明原文句式搬运和术语堆叠不合格。
- `WWH.md` 新增第 8 节表达标准：每段首句为人话、术语延迟解释、抽象落到具体场景、数字给参照系、读两遍不懂即重写；附四组「罗列式 vs 讲清楚」改写示例。顺延编号至第 11 节，版本升为 `WWH-v2`。
- `AGENTS.md` 第 5 节模板说明与第 7 节自检同步加入表达检查。
- 笔记 `jiang2026-jev-mem.md` 按 v2 回填：Why 重写为「场景 → 成本账 → 旧路为何不行 → 可证伪判据」；What/How/Ideas/可复现各加首句人话；补解释 Noul、RRF、记忆表示；front matter 改为 `model: WWH-v2`。

### 2026-10-29 目录命名改为可读形式

- `papers/2609.23986v1/` → `papers/jiang2026-jev-mem/`（`git mv`，保留 PDF 历史）
- `notes/2609.23986v1.md` → `notes/jiang2026-jev-mem.md`；`notes/assets/2609.23986v1/` → `notes/assets/jiang2026-jev-mem/`
- `AGENTS.md` 第 2 节重写命名约定：作者+年份+短标题，arXiv 编号不进目录名，历史编号目录一律改名；第 0 节示例路径、第 6 节索引表（新增 `arxiv` 列）、第 8 节 scope 示例同步更新
- `README.md` 索引改为可读 id + arXiv 链接单列；笔记 front matter 的 `arxiv` 补到 `v1`

### 2026-10-29 引入 WWH 阅读模型

- 新增 `WWH.md`：`WWH-v1`，定义四段职责、阅读顺序（Abstract → Conclusion → Introduction → 方法/实验 → Ideas）、按论文类型分派的 How 清单、Ideas 三步推导与创新点四要素、产出契约与自检。
- `AGENTS.md` 接入：目录树、工作流、第 5 节模板（四段骨架 + `model` 字段）、自检清单、`docs(model)` 提交类型、第 10 节优先级（与第 5 节冲突时以 `WWH.md` 为准）。
- 笔记 `jiang2026-jev-mem.md` 按四段重组：补出 6 条创新点（控制层归因实验、阈值校准迁移、冲突感知合成、学习式控制策略、统一成本口径、轨迹记忆扩展），每条含主张/关系/最小验证/失败条件。

### 2026-10-29 精读 Jev-Mem

- 初始化 uv 环境（Python 3.12 + pymupdf），新增 `tools/pdf_extract.py`、`tools/pdf_figure.py`。
- 提取全文（16 页），裁剪 Fig. 1、Fig. 2 至 `notes/assets/jiang2026-jev-mem/`。
- 产出笔记（status: done），创建 `README.md` 索引。
- 记录原文疑点：§4.2 正文数字与 Table 1 不一致（Multi-Hop 0.625/0.623、Open-Domain 0.610/0.618、Single-Hop 0.797/0.802）；正文声称 Temporal 追平 0.650 但表中为 0.637；§4.1 称两个数据集但只报告 LoCoMo；无消融实验。

### 2026-10-29 仓库初始化

- 建立 `AGENTS.md`：仓库边界、相对路径、目录与命名、uv-only、笔记模板、提交规范。
- 初始化 git，默认分支 `main`；添加 `.gitignore`。
- 将论文 PDF 归档为 `papers/<paper-id>/paper.pdf`。
- 提交：`2a8bee1`（规则）、`93f8f22`（原文）。

## 下一步

- [ ] 按第 8 节拆分提交：`build(deps)`（uv 环境与脚本）、`docs(model)`（WWH 模型）、`chore(repo)`（AGENTS 接入与命名规则）、`notes(jiang2026-jev-mem)`、`docs(index)`、`docs(status)`。
- [ ] 核对代码仓库 <https://github.com/libingzheren/Jev-Mem> 是否公开、是否给出第二数据集与消融。
- [ ] 若确认正文数字与表格冲突，追加 `fix(jiang2026-jev-mem)` 提交修正笔记措辞。
- [ ] 下一篇论文起，按 `WWH.md` 第 3 节顺序阅读，front matter 填 `model: WWH-v2`。

## 阻塞 / 待确认

- 历史提交 `93f8f22` 的信息仍使用旧编号 `2609.23986v1`。不回改已推送历史；若需要统一，另做一次说明性提交。
