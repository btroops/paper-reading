# 仓库状态

> 所有 agent 开工前先读本文件，收工前更新。规则见 `AGENTS.md` 第 9 节。

## 当前快照

- 分支：`main`（跟踪 `origin/main`）
- 远程：`origin` → `git@github.com:btroops/paper-reading.git`
- 最近内容提交：`eaade9c notes(xu2025-sra): 澄清 lossy-context surprisal 的条件集`；`087e2ad notes(xu2025-sra): 解释依存与 surprisal`；`8b615f6 docs(index): 收录 Imperfective Paradox、HySparse2、SRA 三篇`；`c8118d1 notes(xu2025-sra): 用依存局部性检验记忆资源的战略分配`
- 已归档论文：21 篇（`ma2026-imperfective-paradox`，arXiv 2601.09373v3；`wei2026-hysparse2`，arXiv 2609.26368v1；`xu2025-sra`，arXiv 2503.14728v2；`fu2025-c2c`，arXiv 2510.03215v2；`guo2026-t-mem`，arXiv 2606.15405v2；`xia2026-rrsi`，arXiv 2609.24972v3；`zhou2025-onerec`，arXiv 2506.13695v4；`liu2025-onerec-think`，arXiv 2510.11639v2；`onerec2026-onereason`，arXiv 2606.06260v1；`jiang2026-jev-mem`，arXiv 2609.23986v1；`he2026-memory-tax`，arXiv 2610.34073v1；`bao2026-raw-rag`，arXiv 2610.30755v1；`yeh2026-oat`，arXiv 2607.12747v2；`wan2026-decision-rag`，arXiv 2610.35868v1；`wang2026-rsi-hub`，arXiv 2610.32253v1；`li2026-oo-harness`，arXiv 2610.28380v1；`kumar2026-stair`，arXiv 2609.03874v2；`ho2026-declarative-attention`，arXiv 2609.02737v2；`du2026-a-rag`，arXiv 2602.03442v1；`li2026-dci`，arXiv 2605.05242v1；`hu2026-sage`，arXiv 2602.05975v2）
- 已精读论文：21 篇（`ma2026-imperfective-paradox`、`wei2026-hysparse2`、`xu2025-sra`、`fu2025-c2c`、`guo2026-t-mem`、`xia2026-rrsi`、`zhou2025-onerec`、`liu2025-onerec-think`、`onerec2026-onereason`、`jiang2026-jev-mem`、`he2026-memory-tax`、`bao2026-raw-rag`、`yeh2026-oat`、`wan2026-decision-rag`、`wang2026-rsi-hub`、`li2026-oo-harness`、`kumar2026-stair`、`ho2026-declarative-attention`、`du2026-a-rag`、`li2026-dci`、`hu2026-sage`）
- 阅读模型：`WWH-v9`（`WWH.md`），新增不许偷懒省字规则（指代落地、比较写全两边、数字写清口径）；v8 的论证不跳步、v7 的术语与反直译规则继续有效；Why 只提问、What 不写机制、段落 3–6 句
- 命名规则：`<第一作者姓><年份>-<短标题>`，arXiv 编号只写在 front matter 与 README 索引
- Python 环境：uv + Python 3.12，已装 `pymupdf`（`pyproject.toml` / `uv.lock` 已提交）
- 原文策略：PDF 仅本地保存，`papers/` 已被 `.gitignore` 排除，远程只保留笔记与索引
- 进行中：无；Imperfective Paradox / HySparse2 / SRA 三篇已完成并提交（`9b51332`、`8f1ef1b`、`c8118d1`、`8b615f6`）

## 最近会话

### 2026-11-09 精读 Imperfective Paradox / HySparse2 / SRA（语义、长上下文、心理语言学）

- 归档与命名：三篇 PDF 原在仓库根目录。`2601.09373v3.pdf` → `papers/ma2026-imperfective-paradox/paper.pdf`（第一作者 Ma，2026，现象 Imperfective Paradox）；`2609.26368v1.pdf` → `papers/wei2026-hysparse2/paper.pdf`（第一作者 Wei，2026，方法 HySparse2）；`2503.14728v2.pdf` → `papers/xu2025-sra/paper.pdf`（第一作者 Xu，2025，方法 SRA）。全文 19 / 16 / 62 页，已提取 `paper.txt`，按 WWH-v9 产出 `notes/ma2026-imperfective-paradox.md`、`notes/wei2026-hysparse2.md`、`notes/xu2025-sra.md`（均 status: done）。
- 判型：Ma 实证与基准类为主（400 例诊断集、7 模型、4 种提示、5 个规模），附系统与算法类（数据集构造与指标）；HySparse2 系统与算法类为主（混合注意力架构、两级 KV 共享、prefill/decode 分离），附实证与基准类（80B-A3B、290B-A8B、长上下文与 agent 轨迹）；SRA 理论推导类为主（高斯编码-贝叶斯解码、资源约束下的最优分配），附实证与语料基准类（10 种 UD 语言、两个英语阅读时间语料）。
- 核心数字（Imperfective Paradox）：零样本 Group C（终结性 + 不中断，正确 Unknown）的 TBRC 多数 0.94–1.00，Qwen2.5-7B 例外 0.53；Group D（非终结性 + 不中断，正确 True）0.97–1.00；ΔAA 多数 0.00–0.06，Qwen 0.44。Group A（终结性 + 明确中断，正确 False）准确率 0.03–0.47、TBRA 0.46–0.75。DAP 对 Llama C 0.02→0.36、Qwen 0.47→0.89；CoT 把 C 拉高但 D 掉（Llama 0.98→0.65、Qwen 0.97→0.37、Gemma 1.00→0.15）；反事实把 C 拉到 0.97–1.00 但 D 到 0.00–0.10。Qwen2.5 1.5B/7B/14B/32B/72B 的 TBRC 1.00/0.53/0.61/0.09/0.16，ΔAA 0.00/0.44/0.37/0.83/0.81。BERT 表示相似度与 TBRC 的 r=-0.93、p=0.07。
- 核心数字（HySparse2）：80B-A3B，后训练相对 HySparse 平均 MRCR-v2 +11.30、RULER-v2 +19.81；相对 Hybrid SWA +6.44 / +18.65；256k RULER-v2 58.45 对 32.61 / 35.74。1M token prefill FLOPs 2.92× / 5.02×，KV-Cache 2.69 / 6.72 / 12.09 GB。token-level vs block-level：RULER-v2 56.13 对 49.56、两针 MRCR-v2 21.08 对 12.94、GraphWalks 34.92 对 29.38；代价是 BBH −1.23、NoLiMa −1.84。相对 HySparse，预训练 DROP −4.79、GSM8K −2.20、WinoGrande −2.37、MATH −1.82。
- 核心数字（SRA）：Study 1 用 UD 2.11 的 10 种语言，先行词 surprisal 对依存距离的正效应在 6/10 语言显著（丹麦、英语、德语、意大利、俄语、西班牙），4/10 负效应（日语、韩语、汉语、土耳其语）；主语关系 5/10 正效应，宾语关系按词数计 0 种语言正效应（意大利语按 surprisal 计部分支持）。Study 2a（Natural Stories，181 人）在全部/主语关系上发现负的 L×surprisal 交互；Study 2b（Dundee，10 人）只在主语关系第一遍阅读上看到负交互，基线局部性效应本身不稳。理论：高斯编码-贝叶斯解码下，固定总精度时更意外的输入应获得更高编码精度（Appendix A.2）。
- 原文疑点（已写入各笔记 Ideas）：Ma 的 Group C 金标签是理论语义学的 Unknown，人工评估只查语法/流利/充分，没有人类逻辑标注；表示分析用 BERT 而非被评测 LLM；r=-0.93 的 p=0.07；规模分析只有 Qwen2.5；提示条件不是单变量；模型只覆盖 7–9B、英语、模板句。HySparse2 的主对比同时改了头配置（MQA 64/1/256 vs GQA 64/4/192/128），KV-Cache/效率收益不能全归给两级共享；通用能力有 2–5 分下降；没有端到端 agent 成功率；FLOPs/KV 是静态计数，不是延迟。SRA 的词频控制用英语 norms 覆盖 10 种语言；120 个检验无多重比较校正；主语/宾语子集用线性模型、全部关系用 LME，口径不一致；6/10 正效应不能写成"普遍规律"；产生侧可能是 audience design/UID；理解侧有交互无主效应；surprisal 来自 GPT-3/mGPT；高斯推导是理想化。
- 交叉引用：Ma 与 `he2026-memory-tax` 只在"记忆有成本、要分配"的概念上类比，对象分别是人类工作记忆与 agent 外部记忆；HySparse2 与 `ho2026-declarative-attention`（训练无关的注意力声明 vs 训练出来的稀疏架构）、`fu2025-c2c`（跨模型 KV 融合 vs 跨层 KV 共享）、`hu2026-sage`（长上下文检索质量 vs 底层注意力效率）、`he2026-memory-tax`（FLOPs 节省要减去延迟/传输的税）、`kumar2026-stair`（检索粒度 vs 注意力粒度）互引；SRA 与 `he2026-memory-tax`（人类记忆分配 vs agent 记忆收益/税）、`bao2026-raw-rag`（强基线/同预算的方法论）互引。
- 提交：`9b51332`（Ma 笔记）、`8f1ef1b`（HySparse2 笔记）、`c8118d1`（SRA 笔记）、`8b615f6`（索引）、`087e2ad`（SRA 术语解释）、`eaade9c`（lossy-context 条件集澄清）；本文件随 `docs(status)` 提交。

### 2026-11-09 精读 C2C / T-Mem / RRSI（通信、记忆、harness 三层）

- 归档与命名：三篇 PDF 原在仓库根目录。`2510.03215v2.pdf` → `papers/fu2025-c2c/paper.pdf`（第一作者 Fu，2025，方法 C2C，ICLR 2026）；`2606.15405v2.pdf` → `papers/guo2026-t-mem/paper.pdf`（第一作者 Guo，2026，方法 T-Mem）；`2609.24972v3.pdf` → `papers/xia2026-rrsi/paper.pdf`（第一作者 Xia，2026，方法 RRSI）。全文 29 / 19 / 27 页，已提取 `paper.txt`，按 WWH-v9 产出 `notes/fu2025-c2c.md`、`notes/guo2026-t-mem.md`、`notes/xia2026-rrsi.md`（均 status: done）。
- 判型：C2C 系统与算法类为主（缓存投影、融合、门控、对齐、训练），附实证与基准类（4 个多选题基准、LongBench、GSM8K）；T-Mem 系统与算法类为主（带类型记忆、四阶段构建、触发器索引、级联检索），附实证与基准类（LoCoMo、LoCoMo-Plus、8 组消融）；RRSI 系统与算法类为主（形式化、7 条约束、提议/选择算法），附实证与基准类（8 个基准、3 个领域、2 次独立重复）。
- 核心数字（C2C）：Receiver 固定 Qwen3-0.6B，三组 Sharer 的四基准平均提升 11.00 / 9.64 / 11.88 个百分点；比 T2T 高 5.36 / 4.15 / 3.06 个百分点；加速 3.46× / 1.51× / 14.41×。Oracle：Direct 58.42、Few-shot 63.39、Oracle 62.34；消融四列平均：Single 41.52、Identical 46.41、C2C 47.95（我按 Table 6 计算），跨模型净贡献只有 +1.54；融合器约 478M 参数，T2T 解码 80 token / 1312 ms，C2C 融合 90 ms。
- 核心数字（T-Mem）：LoCoMo 80.26（HyperMem 77.01）、LoCoMo-Plus 74.81（HyperMem 48.63），跨基准 gap 5.45（HyperMem 28.38、Mem0 49.14）；消融 w/o ST+HT 在 LoCoMo 只掉 0.40、在 LoCoMo-Plus 掉 22.19；w/o HT 是 −0.08 / −12.47；构建 9,689 次调用、15.60M token；匹配 HyperMem 管线时 T-Mem 93.70 对 HyperMem 92.73（+0.97）。
- 核心数字（RRSI）：TB2.1 74.2→80.2（+6.0）、SWE 82.0→83.8（+1.8）、Harvey evolve 89.4→90.5（+1.1）/ID 86.9→89.2（+2.3）、JobBench 36.0→40.7（+4.7）、GDPval 48.8→52.3（+3.5）、APEX 34.2→37.9（+3.7）、EngDesign 50.0→54.9（+4.9）、Frontier 17.7→22.0（+4.3）；OOD 平均 39.7→43.6；未正则化 3.80M token/trial，RRSI 2.42M；Harvey 20 轮 32 个候选只接受 4 个编辑。
- 原文疑点（已写入各笔记 Ideas）：C2C 摘要 2.5× 加速对不上 Table 4 的 3.46/1.51/14.41（算术平均 6.46×）；6.4–14.2% 与 §4.2 的 11.00/9.64/11.88 对不上；3.1–5.4% 与 3.06–5.36 对不上；T2T 基线只给一句提示、无训练，与 C2C 的 50 万条监督不可比；Table 12 的 300 步 44.30 高于最终 42.92。T-Mem 的 LoCoMo-Plus 与作者组重叠；LoCoMo 与 LoCoMo-Plus 用不同 QA/judge 协议，5.45 gap 含协议差；匹配管线下只领先 0.97；Bridge（条目×联想）没有独立基准；正文 §4.1 没写 reranker，附录 E 又用了 reranker。RRSI 摘要"up to 4.3 OOD"与 JobBench +4.7 冲突；"30% fewer tokens"按 Table 2 是 36.3%；Harvey 分布内留出与 Meta-Harness 并列 89.2；七个约束只做了两组消融；搜索成本（提议器/critic/候选评估）没有账本。
- 交叉引用：C2C 与 `ho2026-declarative-attention`（都在推理时操作 KV-Cache，一个掩码减少读取、一个融合增加信息）、`li2026-oo-harness` / `wang2026-rsi-hub`（都在改模型外围装置）、`he2026-memory-tax`（成本账本）、`jiang2026-jev-mem`（检索侧减少文本中转）互引；T-Mem 与 `jiang2026-jev-mem`（控制层 vs 索引层）、`he2026-memory-tax`（收益/税）、`bao2026-raw-rag`（强基线）、`hu2026-sage`（语料级增强 vs 写入时触发器）、`du2026-a-rag` / `li2026-dci`（工具接口 vs 记忆索引）、`kumar2026-stair`（结构作为检索单位）互引；RRSI 与 `li2026-oo-harness`（表示 vs 搜索 dynamics）、`wang2026-rsi-hub`（装置 vs 策略）、`yeh2026-oat`（步级归因 vs 轮级反馈）、`he2026-memory-tax`（搜索成本）、`bao2026-raw-rag`（强基线重设参照系）互引。
- 提交：`6750371`（C2C 笔记）、`74569cb`（T-Mem 笔记）、`7530f04`（RRSI 笔记）、`06eb4db`（索引）、`e14364e`（C2C 口径修正）、`c87ced2`（RRSI 归因修正）、`cd9ac99` / `8e1c079` / `91d1d9f`（术语修订）、`a7db4a1`（Why 重写）、`a380956`（proposer 与候选池定义）、`e4efd23`（编辑空间表述）、`f31c5d0`（critic 与噪声带定义）、`380e207`（指代落地）、`6f7fa4c`（分布外收益定义）、`0d77952`（选择次数与噪声偏差）；本文件随 `docs(status)` 提交。

### 2026-11-06 精读 OneRec 三部曲（OneRec / OneRec-Think / OneReason）

- 归档与命名：三篇均为快手 OneRec 团队的技术报告。`2506.13695`（v4，2025-09-16）→ `papers/zhou2025-onerec/`；`2510.11639`（v2，2025-11-11）→ `papers/liu2025-onerec-think/`；`2606.06260`（v1，2026-06-04）→ `papers/onerec2026-onereason/`。全文分别 39 / 17 / 108 页，已提取 `paper.txt`。
- 判型：三篇都以系统与算法类为主，附实证与基准类。OneRec 是单阶段生成式推荐 + 工程效率；OneRec-Think 是"对齐 → 推理激活 → beam 奖励 RL"的三阶段 + Think-Ahead 部署；OneReason 是四粒度预训练 + 三段式 CoT + 专精后统一的推理基座，外加 R0–R3 分层基准。
- 核心数字（OneRec）：训练/推理 MFU 23.7% / 28.8%（基线 4.6% / 11.2%），OPEX 10.6%；接管约 25% QPS，叠加奖励模型选择后 App Stay Time +0.54%（主站）/ +1.24%（极速版），LT7 +0.05% / +0.08%；本地生活 GMV +21.01%。纯 OneRec 的 Like / Follow / Comment 分别为 −2.00% / −2.88% / −1.56%，加选择后才转正。
- 核心数字（OneRec-Think）：公开三数据集十二格全第一，Beauty R@5 0.0563 对 ReaRec 0.0450；消融 Base 0.0460 → +对齐 0.0532 → +推理 0.0563；线上 1.29% 流量、一周，App Stay Time +0.159%、Watch Time +0.169%。
- 核心数字（OneReason）：578B token 三阶段预训练；R3 四个域全第一，Cross-Video Pass@64 2.41 对 LC-Rec-PT-SFT-8B 1.49、Cross-Live 21.10 对 19.32；R0–R2 上 RFT thinking 的 Item2Item 28.60、兴趣动作选择 42.42；通用能力在 thinking 模式基本追平 Qwen3-8B；线上 10 天 A/B 组合部署曝光 +10.332%、收入 +8.234%，ROI > 5，600 张 GPU/天服务 4 亿用户。
- 原文疑点（已写入各笔记 Ideas）：OneRec 的 A/B 只替换降级（缓存）流量，+0.54% / +1.24% 不等于全量实时对比；纯 OneRec 交互指标为负；OPEX 未含 Pass@512 采样与奖励模型；MFU 28.8% 与结论 28.6% 不一致；scaling law 只有曲线无公式。OneRec-Think 公开基准用"人工类别 CoT"替代自生成理由，与正文方法不一致；Table 1 是否含 RL 未写明；消融非单变量；Think-Ahead 缺少随机前缀对照，T / m / 延迟未报。OneReason 的基准由团队自建并用于指导模型；"thinking 稳定更优"在 R0 grounding（1.35 对 5.24）与低 K（RFT Cross-Video R@8 0.05 对 0.06）上不成立；绝对数字极小且无置信区间；RL 超参缺失；教师理由逻辑均分只有 3.51/5。
- 交叉引用：OneRec 与 `kumar2026-stair`（语义 ID vs 目录叶标题）、`du2026-a-rag` / `li2026-dci`（压成单模型 vs 拆成工具接口）、`ho2026-declarative-attention`（把算力集中到该用的地方）、`he2026-memory-tax`（收益/税账本）互引；OneRec-Think 与 `wan2026-decision-rag`（先判断再输出）、`ho2026-declarative-attention`（把隐式过程外化）互引；OneReason 与前三篇及 `hu2026-sage`（基准方法论）、`li2026-oo-harness` / `wang2026-rsi-hub`（先专精再统一）互引。
- 提交：`d293070`（OneRec 笔记）、`364cff4`（OneRec 索引）、`c7d3077`（OneRec-Think 笔记）、`ca4fad3`（OneRec-Think 索引）、`74188e8`（OneReason 笔记）、`1e4ddd7`（OneReason 索引）；本文件随 `docs(status)` 提交。

### 2026-11-05 WWH 升到 v9：不许偷懒省字

- 起因：DCI 笔记用"反向只有 76 道"指代"检索答对而 DCI 答错"，读者无法判断"反向"相对于什么；同类偷懒还包括"前者/后者/该配置/上述"、只写"高 16 点"不写从多少到多少、只写"成本翻倍"不写两个金额。
- `WWH.md` 第 8 节新增规则 13：不许偷懒省字。指代必须落地（把名词再写一遍）；比较必须写全两边（从多少到多少）；数字写清口径（哪一组、哪一边、哪个指标）；判断办法是把句子单独拿给没读过上一段的人看，能否说出"谁、比什么、结果是什么"。补 8.2 反例（"反向只有 76 道"）、8.3 两条自问、第 9 节产出契约与第 10 节自检。
- `AGENTS.md` 模板改为 `model: WWH-v9`，第 7 节自检新增一条。
- `notes/li2026-dci.md` 的逐题配对与工具消融两段改成大白话（去掉"反向/净胜/逐题配对/工具集消融/边际收益/高分辨率接口"），`model` 升到 v9；`notes/hu2026-sage.md` 同步升 v9；A-RAG 保持 v7。
- 提交：`0326fd6`（WWH）、`1075a90`（AGENTS）、`7f57f8f`（SAGE 测试台改写与 v9 标注）、`d3c90c1`（DCI 白话改写）；本文件随 `docs(status)` 提交。

### 2026-11-05 WWH 升到 v8：论证不许跳步

- 起因：SAGE 笔记 Why 里"这套做法在标准基准上更强，因为主要矛盾是语义匹配。但它有一个前提……"被指出前后对不上——"主要矛盾"是未定义标签，"前提"没有交代从哪条原因拆出，读者不知道转折的依据。
- `WWH.md` 第 8 节新增规则 12：论证不许跳步。结论前先给前提；"但是/所以/前提是/条件是"之前必须交代依赖的事实；禁止"先给结论再补条件"；禁止用未定义标签（"主要矛盾""瓶颈""错配"）代替具体判断。补 8.2 正反例（BEIR/MTEB 那段）、8.3 两条自问、第 9 节产出契约与第 10 节自检。
- `AGENTS.md` 模板改为 `model: WWH-v8`，第 7 节自检新增一条。
- `notes/hu2026-sage.md` 的 Why 按新规则改写为三段（基准为什么强 → 同分布是条件 → agent 查询形式使条件不成立），`model` 升到 v8；A-RAG 与 DCI 保持 v7，不回填。
- 提交：`fb29444`（WWH）、`f77bdfa`（AGENTS）、`c554a56`（SAGE 衔接）、`dae4106`（本文件）。

### 2026-11-05 精读三篇 agentic RAG（A-RAG / DCI / SAGE）

- 归档与命名：`papers/ARAG.pdf` → `papers/du2026-a-rag/paper.pdf`（第一作者 Du，方法名 A-RAG）；`papers/DCI.pdf` → `papers/li2026-dci/paper.pdf`（第一作者 Zhuofeng Li，方法名 DCI，注意与 `li2026-oo-harness` 不同人）；`papers/SAGE.pdf` → `papers/hu2026-sage/paper.pdf`（第一作者 Hu，方法名 SAGE）。三篇均提取全文（18 / 51 / 16 页），按 WWH-v7 产出 `notes/du2026-a-rag.md`、`notes/li2026-dci.md`、`notes/hu2026-sage.md`（均 status: done）。
- 处理顺序：先 A-RAG（把检索做成三层工具接口），再 DCI（去掉检索器、直接用终端读原始语料），最后 SAGE（固定语料上比较检索器，发现 BM25 强于 LLM-based retriever）。三篇互引，形成"接口分层 → 接口去掉 → 接口评测"的链条。
- A-RAG 判型：系统与算法类为主（三层索引、三个工具、ReAct 循环、已读集合），附实证与基准类（4 数据集、2 backbone、8 基线、消融、扩展曲线、失败分析）。核心数字（Table 1）：GPT-5-mini 上 A-RAG Full 74.1/94.5/89.7/93.1/85.3（MuSiQue/HotpotQA/2Wiki/Med/Novel 的 LLM-Acc），全面第一；GPT-4o-mini 上 3/5 benchmark 第一（按子集是 4/5），2Wiki 输给 HippoRAG2 64.7 与 LinearRAG 62.9。检索 token（Table 3）：Full 5,663/2,737/2,930/7,678/6,087，Naive 版 56,360/27,455/45,406/23,657/22,391，Naive RAG 5,387/5,358/5,506/5,418/4,997。失败分析（Table 7/8）：A-RAG 82%/45% 错误是推理链错误，实体混淆 40%/71%。
- DCI 判型：系统与算法类为主（接口定义、两个脚手架、上下文管理 L0–L4、覆盖率/定位度指标），附实证与基准类（BrowseComp-Plus 830 题、6 个 QA 数据集、6 个 IR 数据集）。核心数字：BrowseComp-Plus 上 CC 80.0 对 69.0（+11.0），成本 $1,016 对 $1,440（−29.4%）；QA 平均 83.0 对最强检索 agent 52.3（+30.7）；IR 平均 NDCG@10 68.5 对 ReasonRank 47.0（+21.5）。机制证据（Table 4）：100 题子集上 DCI-Lite 覆盖率 28.0 对 56.7、定位度 48.4 对 21.7、准确率 73.0 对 45.0；逐题配对 176 胜 / 76 负，176 个胜场里 142 个检索已找到至少一篇 gold 却答错（83 部分链、59 检索后失败）。
- SAGE 判型：实证与基准类为主（1,200 题、4 域、20 万篇、两套指标），附系统与算法类（语料级增强流程、DR Tulu MCP 改造）。核心数字（Table 2）：短答案 top-10 上 BM25 81.2、gte-Qwen 63.0、ReasonIR 49.3；BM25 对 gte-Qwen 是相对 +28.9%（绝对 +18.2 点），摘要的"约 30%"指这个相对值；开放式上 gte-Qwen 33.0 略高于 BM25 30.7。语料级增强（Table 4）：BM25 短答案 75.80→83.98（+8.18 绝对点），开放式 25.52→27.25（+1.73）；稠密检索器提升 0.90–2.54 点。消融（Table 3）：网页搜索下 agent 最依赖图表细节，语料搜索下最依赖论文间关系。
- 原文疑点（已写入各笔记 Ideas）：A-RAG 的 Full/Naive 同时改了提示词、w/o Chunk Read 不是单变量、关键词打分无 IDF、只报检索 token、§5.1 用 GPT-5 与 Limitations 冲突；DCI 的 CC 与检索基线 harness 不同、QA 基线模型代差大、IR 非同预算、定位度指标偏向细粒度接口、语料 20 万篇掉 13.6 点、答案泄漏防护只写了 CC；SAGE 的问题由 GPT-5-mini 生成无人工校验、EM/加权召回不惩罚多余文档、问题与语料同源、稠密检索只编码 32K token、摘要 30% 与 8%/2% 的口径、网页与语料搜索不可直接比。
- 交叉引用：A-RAG 与 DCI 都反对固定 top-$k$，区别是保留还是去掉向量索引；SAGE 的"BM25 强于稠密"为前两篇的"词面接口"提供评测证据；三篇都与 `wan2026-decision-rag`（层级检索控制器）、`kumar2026-stair`（结构作为检索单位）、`bao2026-raw-rag`（强基线重设参照系）、`he2026-memory-tax`（成本账本）互引。
- 补充：用户反馈 SAGE 的 Why 里"用大模型做稠密编码"看不懂，新增 `notes/concepts/dense-retrieval.md`（BM25 公式、token 向量与池化、InfoNCE 对比学习、取隐藏状态/指令微调/推理链扩展三种做法、agent 场景的四个失效机制、读论文检查清单），并改写 `hu2026-sage` 的 Why 前两段；Ideas 新增一条"gte/ReasonIR 是否加指令模板"的方法疑点（编号顺延为 18 条）。
- 提交：`a34d09f`（A-RAG 笔记）、`62f140d`（A-RAG 索引）、`0f35440`（DCI 笔记）、`8657bcf`（DCI 索引）、`ed7a126`（稠密检索概念）、`3bd4782`（SAGE 笔记）、`df5d09c`（SAGE 索引）；本文件随 `docs(status)` 提交。

### 2026-11-04 论文原文改为仅本地保存

- `papers/` 整目录加入 `.gitignore`，`git rm --cached` 停止跟踪 9 篇 PDF（约 28 MB），本地文件全部保留。
- 规则同步：`AGENTS.md` 删除 `paper` 提交类型，一篇论文的提交降为 `notes` + `docs(index)` 两次；`README.md` 说明 clone 后按 arXiv 链接自行下载原文。
- 已重写历史：`filter-branch` 从全部提交中删除 `papers/`，提交数 104 → 94（原文归档与纯移动提交变空被丢弃）；所有 hash 变化，本文件内引用已同步为新值，原文 hash 直接删除。
- 备份分支 `backup/pre-pdf-rewrite` 仅存本地；`main` 以 `--force-with-lease` 覆盖远程。

### 2026-11-04 精读 Declarative Attention（模型自控注意力）

- 归档：`papers/2609.02737v2.pdf` → `papers/ho2026-declarative-attention/paper.pdf`；`paper-id` 取第一作者姓 `ho` + 年份 + 方法名 `declarative-attention`。提取全文（43 页，正文 14 页 + 附录），按 WWH-v7 产出 `notes/ho2026-declarative-attention.md`（status: done）。
- 判型：系统与算法类为主（协议、状态机、vLLM 块表实现、屋顶线成本模型），附实证与基准类（15 源、6 模型、DAnm 对照、LLM judge）；无定理、无新训练目标、不训练模型。
- 核心贡献：让现成模型在思维链里用 `<global>`、`<focus magic_chunks="K">`、`<local>` 三种标签声明注意力范围，引擎按标签改 KV 块表；零样本、一个固定提示词、15 个长上下文源、两个模型家族、最长 244K。
- 主结果（Table 2）：Gemma-4-31B 的 attended tokens 13.84M→7.49M（-45.8%），准确率 86.49%→85.09%（-1.40pp）；Qwen-3.6-27B 22.34M→17.88M（-19.6%），84.92%→82.83%（-2.10pp）。DAnm（同提示词、全注意力）准确率 87.01/84.88、token 比 vanilla 高 50.2%/35.2%，说明节省来自掩码。
- 效率：屋顶线 0.76×/0.87×（Table 3）；实测每步在掩码比例 >90% 的箱省 55%/31%，0–10% 箱慢 3.5%/3.9%（Table 11）；Gemma 的 SWA 局部读占 DA 注意力时间 39%，Qwen 的 GDN 只占 5%。
- 规模与上下文：相对准确率随模型变大收敛（Gemma 29%→98%，Qwen 64%→98%）；attended tokens 占 vanilla 的比例不单调（Gemma 46.0/183/54.2，Qwen 50.3/67.7/80.4；换算成节省是 54.0/-83/45.8 与 49.7/32.3/19.6；12B 去掉 6% 非终止回答后是 98%）；绝对节省随上下文升到约 19M（Fig. 4）。
- 失效边界：15 源是按"DA 有效"选出的，另 6 源掉准确率或不省 token（Table 12）；DSA 上每步扫描 0.46×，但步数 2.78×，总扫描 1.28×；thinking 模式不遵守协议，全部结果 non-thinking；E4B focus 成功率 58%。
- 原文疑点（已写入 Ideas）：15 源选择偏差——我按每源等权估算全 21 源，Gemma 准确率 79.86→76.28（-3.58pp）、attended tokens 只省 11.6%；3 次运行只重采样生成、不重采样题目，judge 分歧率约 1.5% 与 1.40pp 同量级；只算 decode、不算 prefill 与端到端；没有和 Quest/H2O/DSA 同预算对比；掩码只限制全局 KV 读，prefill、SWA/GDN、已生成回复仍携带上下文，local 不是信息隔离；token 节省不随规模稳定；global 步仍占 80% 以上 attended tokens；两类结构性失效（切块破坏证据、输出随文档变长）的补救未实验；DSA 扫描数是重建的，非法 focus 回退未写，提示词开发集未报。
- 交叉引用：`wan2026-decision-rag`（同为候选集内选一支，选择发生在生成前 vs 生成中）、`kumar2026-stair`（结构作为检索单位 vs 注意力单位）、`he2026-memory-tax`（收益/税账本，DA 只报了部分税）。
- 提交：`596b6ee`（notes）、`2247b74`（docs(index)）；原文归档提交已在历史重写中移除；本文件随 `docs(status)` 提交。

### 2026-11-04 统一各笔记的任务定义

- 起因：STAIR 笔记被反馈"读完看不出任务是'问题 + 指定书的目录 → 叶标题'"，说明 What 开头只给答案、没有交代输入输出；检查其余 7 篇，问题相同，读者要靠 How 的形式化自己拼。
- 改动：在每篇 What 开头补一段任务定义，写清输入、输出与边界，不改事实、数字、锚点与结论。
- 逐篇口径：`jiang2026-jev-mem` 多会话历史 + 问题 → 答题模型写答案；`he2026-memory-tax` 有记忆 vs naive RAG 的逐题配对；`bao2026-raw-rag` 原始历史 + 问题 → 答案；`yeh2026-oat` 执行轨迹 → 步级异常分与疑似步骤集合；`wan2026-decision-rag` 查询 + 已建好的树 → 前 k 段；`wang2026-rsi-hub` 配方 + seed agent + 基准 → 候选 commit 与档案；`li2026-oo-harness` 任务 + 基座 harness + discovery → harness 树与路由。
- 未改：`model` 字段保持原版本（这次只补任务定义，不做 v7 全篇回填）。
- 提交：`65fa32a`、`5f90fb9`、`f945a5b`、`988942b`、`188b062`、`8e58699`、`ccad0f9`，每篇一个；本文件随 `docs(status)`。

### 2026-11-04 精读 STAIR（目录检索）

- 归档：根目录的 `2609.03874v2.pdf` → `papers/kumar2026-stair/paper.pdf`；`paper-id` 取第一作者姓 `kumar` + 年份 + 方法名 `stair`。提取全文（11 页，正文 8 页 + 参考文献），按 WWH-v7 产出 `notes/kumar2026-stair.md`（status: done）。
- 判型：系统与算法类为主（问题形式化、三阶段流水线、约束解码），附实证与基准类（自建 SearchTome、五个基线、两组按样本量分层的观察）；无定理、无新训练目标、不训练基座。
- 核心贡献：把目录叶节点同时当作检索单位和文档标识符，微调 Mistral 7B 在"查询 + 整份目录"上直接输出叶标题，推理时把输出限制在合法叶标题上。
- 主结果（Table 4）：Recall@1 82.6 对 DSI 76.9（+5.7 点；摘要的 +7.4% 是相对增益）、DPR 68.7、BM25 59.5、Haiku 4.5 为 45.6、未微调 Mistral 13.8；Recall@3 90.8、nDCG@3 87.5；6 个领域全部领先 DSI，差距 4.0–7.5 点。
- 基准规模（我按 Table 1 加总）：18 本书、6 个领域、2,880 个叶、12,475 页、190,209 道题；train 32.8% / dev 12.9% / test 54.3%；每叶平均 21.7 道训练题、35.9 道测试题。
- 原文疑点（已写入 Ideas）：目录在输入里，"知识入库"没有被隔离；缺"零样本 + 目录 + 约束解码"、标题向量检索、数字 docid DSI 三个基线；合成 gold 无人工校验，题目按段落聚集，随机化检验的独立样本假设不成立；0.05% 非叶输出与 Stage 3 约束解码冲突，Fig. 3 上 STAIR 也有 0.1–0.2% 的小峰；§4.1 叶节点公式按字面读把"叶"写反了；错误率与 Recall@1 的补数对不上（18.67 对 17.4、24.31 对 23.1）；Haiku 无设置、Mistral 输入未写、STAIR 是否每书微调未写；无延迟、算力、费用。
- 交叉引用：`wan2026-decision-rag`（同为候选集内选分支，控制器不同）、`bao2026-raw-rag`（基线强度与参照系）、`he2026-memory-tax`（缺成本账本）。
- 反馈修订：Why 里讲 DSI 的那段被指出"完全没看懂"，已重写为四段：先讲参数化索引怎么训练与查询，再讲为什么逐字回忆容易错，用 Table 3 例 1 的拼接标题说明，最后引出"结构"这个缺口；补 DSI 与 DPR 的全称。第二轮反馈指出"结构"那段仍不懂，又把该段拆成两段：先讲 DSI 没见过整份目录、只能凭反推出来的关联表作答，再用 "preschoolers" 对 "Preschool Years" 的逐条对照说明候选清单的作用。第三轮追问叶节点长什么样、目录在训练还是检索时输入、为什么输入就有效，已在 How 三补 Table 3 的真实目录片段（标出叶与非叶）、说明训练与检索共用同一模板、正文只在造题与取文时使用。第四轮指出读完笔记仍看不出任务是"问题 + 指定书的目录 → 叶标题"，已把任务定义前置到 What 开头，并在 How 一补三个边界（书是输入、粒度到节、输出是标题）。
- 提交：`b9c69a9`（笔记）、`beabaae`（索引）、本文件随 `docs(status)`；修订另提交 `notes(kumar2026-stair)` 与本文件。

### 2026-11-03 WWH 升到 v7：术语与反直译

- 起因：读 DecisionRAG 与 OO-Harness 笔记时，出现"用写代码、跑测试、看反馈的方式来搜索""加入进化出来的记忆"这类直译；术语首次出现不定义、后面换同义词，读者对不上。
- `WWH.md` 第 8 节新增规则 10（术语首次定义、之后全篇同名、缩写首现写全称）与规则 11（反直译：翻回英文若逐词对应就重写；动词要有宾语；名词堆叠要拆开），并补 8.4/8.5 的正反例；产出契约与自检同步。
- `AGENTS.md` 模板改为 `model: WWH-v7`，第 7 节自检新增两条。
- 旧笔记不强制回填；`wan2026-decision-rag` 仍为 v6，`li2026-oo-harness` 已在本次自检中改为 v7。
- 提交：`f86abb5`（模型）、`28fdc45`（自检）、本文件随 `docs(status)`。

### 2026-11-03 精读 OO-Harness（面向对象的 harness 进化）

- 归档：根目录的 `2610.28380v1.pdf` → `papers/li2026-oo-harness/paper.pdf`；`paper-id` 取第一作者姓 `li` + 年份 + 方法名 `oo-harness`。提取全文（20 页），按 WWH-v6 产出 `notes/li2026-oo-harness.md`（status: done）。
- 判型：系统与算法类为主（类层级表示、簇级搜索、路由函数、接受条件），附实证与基准类（三基准端到端 + 两组消融 + OOD）；无定理、无新数据集、不训练模型。
- 核心贡献：把专家 harness 做成基座或已有专家的**子类**（继承 + 覆盖 + `super()`，单实例执行、祖先不是额外 rollout），并用"任务 + 基座轨迹 + 冻结路由教训"选择；训练只在目标簇上评估候选。
- 主结果（Table 1）：Automation Mean 77.41 对基座 61.62（摘要的 +15.79 即是此差）、AAH 75.40；Workspace Mean 39.48 对 AAH 38.62、AHE 38.43；Toolathlon PASS 37.45 对 AHE 36.23、AAH 34.32。搜索时间 29.0 h 对 Meta-Harness 109.1 h（Fig. 4b）。
- 机制诊断：路由输入加基座轨迹，Automation +12.64、Toolathlon +4.37、Workspace 仅 +0.53（Table 2），原因是 Workspace 的簇与 AAH 任务类型一一对应（Fig. 6b）；继承 ablation 29.39 / 35.60 / 40.56（Fig. 5，+4.96）；基座复用 134/300（44.7%）时基座均分 77.15 对 44.40（Table 3）。
- 原文疑点（已写入 Ideas）：OO 与 AAH 差继承、聚类依据、路由依据三件事，只拆了后两件，最大领先恰落在没拆的那维；Workspace 与 Toolathlon PASS 的领先在 1 点上下，小于执行器标准差，且三次重跑不覆盖搜索方差；Steps 排除基座 rollout 与路由调用，测试期成本无账本；§4.1 与 A.4.2 的路由模型口径冲突（Sonnet 5 vs Opus 4.8）；OOD 实验 49 题全选基座，OO 分数按构造等于基座；接受规则、接受节点数、簇规模、教训是否启用均未报告；每基准一套 harness，不跨基准迁移。
- 交叉引用：`wang2026-rsi-hub`（装置 vs 策略，缺同一套可审计纪律）、`wan2026-decision-rag`（同为"候选集 + 证据选择"的控制器）、`yeh2026-oat`（路由教训是任务级失败归因，粒度更粗）、`he2026-memory-tax`（收益/税账本）、`bao2026-raw-rag`（强基线重设参照系）、`jiang2026-jev-mem`（同为控制层）。
- 提交：`1dfde21`（笔记）、`211cc09`（索引）、本文件随 `docs(status)`。
- 自检与补充：`f0ace26`（笔记）——`model` 升到 v7，补“描述路由 vs 轨迹路由”说明；本文件随 `docs(status)`。

### 2026-11-03 精读 RSIHub（智能体进化框架）

- 归档：PDF 原先误放在 `notes/2610.32253v1.pdf`，已移至 `papers/wang2026-rsi-hub/paper.pdf`；`paper-id` 取第一作者姓 `wang` + 年份 + 方法名 `rsi-hub`（注意与 `wan2026-decision-rag` 的第一作者 Wan 不同人）。提取全文（19 页），按 WWH-v7 产出 `notes/wang2026-rsi-hub.md`（status: done）。
- 判型：系统与算法类为主（协议、生命周期、认证记录、恢复语义），附实证与基准类（4 方法 × 2 agent × 2 基准的描述性对比）与实验方法学（故障注入、能力保持对照）。
- 核心贡献：把"进化策略"与"执行装置"拆开。配方按七个阶段绑定九个算子（五必需：Select / Rollout / Mutate / Gate / Record；四可选：Analyze / Validate / Novelty / Reflect），声明可变面与运行配置；评测与存档在可变面之外，每次评测绑定候选 commit、父代、配方快照与三层指纹。
- 主结果（Table 1 / 2 / 3 / 5 / 6）：Terminal Bench 2 + MiniSWE 从 56.2 到 69.7（+13.5），Codex 从 69.7 到 71.9（+2.2）；τ 3 Banking 上 A-Evolve 为 0.0、AHE（Codex）为 +9.3。能力保持 Avg@3 差 −2.7 / −2.6 / −2.6 / +3.4，逐题一致率 80.1–84.6%，直接执行彼此不一致 12.0–18.9%。故障注入 7 场景 × 2 基准 × 30 次 = 420 次全部通过。框架自身开销占一次生成时间 0.02%（TB2 中位）/ 0.019%（τ 3）。四个配方 47–61 行、0 个框架文件改动，方法特有算子 216–1087 行。
- 关键换算（我自己做的，论文未给）：Table 1 每格是 $N_{\text{pass},s}/N_{\text{all}}$，乘回 89 / 97 均为整数，所以 Terminal Bench 2 一道题值 1.12 点、τ 3 Banking 一道题值 1.03 点；+1.1 就是一道题，13.5 点约 12 道题，正好落在 §4.4 测出的 11–18 题翻转带里。
- 原文疑点（已写入 Ideas）：主表单次运行无区间，与自测翻转率同量级；无"同预算不进化"对照且不报成本（档案已记成本、配方有 budget_usd: 150）；四个配方是本文重写而非原方法代码；§4.1 介绍的 hill_climb 基线未进 Table 1；headline 取自最弱 seed；agent-driven 模式零实验；完整性测试未覆盖"候选改自己的 Gate"（§3.2 明说 Gate 从 committed child 加载）；工程量无反事实；Table 5 两 campaign 的 init / snapshot 成本方向相反；Table 2 的 TB2/MiniSWE 写 −2.6 实际 −2.7；Table 1 用 "%" 表示 percentage points。
- 交叉引用：`he2026-memory-tax`（收益/税账本，本文缺成本分母）、`bao2026-raw-rag`（强基线重设参照系，对应本文缺的同预算对照）、`yeh2026-oat`（可接成 Analyze 算子）、`jiang2026-jev-mem` 与 `wan2026-decision-rag`（都是换判断器，本文换装置，不同层）。
- 新增概念笔记 `notes/concepts/agent-evolution.md`：解释进化改的是仓库文件而非权重、一轮进化的五道工序、四个代表方法改什么、三个易混概念（微调 / 提示优化 / 搜索），以及这类实验容易自欺的五条路径与读论文时的五问清单。论文笔记 Why 第一段已链接该文。
- 2026-11-03 按 WWH-v7 回填：`model` 升到 `WWH-v7`；全篇统一术语（进化、阶段、配方、算子、可变面、档案、准入、改写、检出、回执、契约、sealed），首次出现补定义与英文全称（AHE、GEPA、RQ、LOC、pass@1、Avg@3、best-of-$k$、bootstrap、genesis、anchor、coverage policy），并改写若干直译句；概念笔记同步统一术语。事实、数字与锚点未变。
- 提交：`74036fc`（笔记）、`2d5a010`（概念）、`0ce8c7e`（索引）、本文件随 `docs(status)`；v7 回填待单独提交 `notes(wang2026-rsi-hub): 按 WWH-v7 统一术语`。

### 2026-11-03 精读 DecisionRAG（决策模型检索）

- 归档：`papers/2610.35868v1.pdf` → `papers/wan2026-decision-rag/paper.pdf`；`paper-id` 取第一作者姓 `wan` + 年份 + 方法名 `decision-rag`。提取全文（21 页），按 WWH-v6 产出 `notes/wan2026-decision-rag.md`（status: done）。
- 判型：系统与算法类为主，附实证与基准类；核心贡献是把层级检索每一层的"展开哪一支"从生成式 LLM 换成决策模型（Jev），并用共享上下文让逐候选判断可比，不是提出新的语料树结构。
- 主结果（Table 2 / Table 3 / Table 5）：对"Dense top-100 + Qwen3-Reranker-8B"，MultiDoc2Dial R@1 47.4 对 33.6（+13.8），NQ Hit@1 65.4 对 48.0（+17.4）；单查询 0.68–1.76 s、0.22–2.33 美分。ConditionalQA 上 GPT-5 列表式重排 73.4 高于本文 69.7；MTRAG R@5 34.2 对最好基线 32.5（加稠密候选 36.6）。端到端 MTRAG 判对率 39.4%→44.1%（加稠密 47.3），NQ EM 52.4→54.2（gold 65.3）。
- 原文疑点（已写入 Ideas）：§6.5 的"导航 vs 重排"同时改了候选集与呈现形式（整页阅读顺序），归因未单独验证；主表无置信区间；延迟对比混用实时 API、单卡本地与只算重排的 GPT-5，作者自注不是受控加速比；主实验绑死专有 Jev；NQ 设计题来源未写明；MTRAG 的 GPT-5 扩标池深（top-5）等于 R@5 指标深度；论文未给代码链接。
- 交叉引用：与 `jiang2026-jev-mem` 同用 Jev、方向相反（记忆控制 vs 检索导航）；`bao2026-raw-rag` 的"稠密加交叉编码器"强基线正是本文拉开 13.8 / 17.4 点的那条线；`he2026-memory-tax` 的收益/税账本可补本文缺的建树成本。
- 反馈修订：初版被指出"直译、看不懂"，按 WWH-v6 第 8 节重写全文。先给 Nolan 查询这个具体场景，再命名概念；R@k / Hit@k / nDCG 与 gold、决策模型、共享材料、池化、bootstrap、LoRA 都在首次出现时解释；长句拆短，How 把"走一遍"提到开头；事实、数字与锚点未改。
- 提交：`63ac61b`（笔记）、`ddd6cc8`（索引）、本文件随 `docs(status)`。

### 2026-11-02 推送至 GitHub

- 配置 `origin` 为 `git@github.com:btroops/paper-reading.git`，SSH 认证通过。
- 远端此前为空，直接推送 `main` 全量历史并建立 `origin/main` 跟踪，无历史冲突。
- 未执行 GitHub 模板里的 `git init`、`first commit` 与追加 README 标题：仓库已有完整历史与索引，重复初始化会产生不符合第 8 节规范的提交。

### 2026-11-02 精读 OAT（智能体失败归因）

- 归档：`papers/2607.12747v2.pdf` → `papers/yeh2026-oat/paper.pdf`；`paper-id` 取第一作者姓 `yeh` + 年份 + 方法名 `oat`。提取全文（25 页），按 WWH-v6 产出 `notes/yeh2026-oat.md`（status: done）。
- 判型：系统与算法类为主，附实证与基准类；核心贡献是把失败归因改写成"只用成功轨迹的单类异常检测"，并把轨迹当连续时间过程建模。
- 主结果：MCP-Atlas 上 OAT（共形）F1 0.435，对 GPT-4o 0.212、GPT-5 0.181；Who&When 上 top-k F1 0.225，对 GPT-5 0.152；推理 0 输出 token、7–16 ms，基线 4.2–39.6 s（Table 1–3）。
- 原文疑点（已写入 Ideas）：摘要称用 100 条成功轨迹训练，正文与附录 D 为 103 条；相对 Isolation Forest 只高 2.4 点 F1（0.435 对 0.411）；GPT-5 域内 F1 0.181 低于随机基线 0.255，提示基线可能未调；没有监督式方法对照；域外主数字用全测试集拟合 CORAL，五折只在 Fig. 12；步级标签由作者自标、无一致性统计；平均轨迹 7 步与"几十到几百步"的动机不符；200–5000× 不含隐状态提取（实际约 1000 ms/条）。
- 交叉引用：与 `he2026-memory-tax`、`bao2026-raw-rag` 同属"如何度量 agent 系统可靠性"，但对象不同；仓库暂无同主题笔记。
- 新增概念笔记 `notes/concepts/failure-attribution.md`：展开 Why 里被压缩的两句——三种"部分补偿"形态（前提污染、局部修复、覆盖重写）、为什么最后一步是症状而非病因、以及诊断成本如何卡住部署/调试/审计；OAT 笔记 Why 第一段与第二段均已链接该文（第二段指向第四节）。后补第四节（`5f3dd1d`）：提示式、监督式、干预式分别按"每次诊断 / 每个标签 / 每次重放"付费，附四类方法对比表。
- 提交：`fbeb3ad`（笔记）、`2bd84c1`（概念）、`e500ba5`（引用）、`5f3dd1d`（第四节）、`6bbd505`（引用修复）、`d67f428` / `68b4f48`（索引）、本文件随 `docs(status)`。

### 2026-11-02 修正 RAW-RAG 公式渲染

- 现象：Ideas 创新点四的三处 `$N^\*$` 在预览中报 `KaTeX parse error: Undefined control sequence: \*`。
- 原因：`\*` 不是 KaTeX 合法控制序列，上标星号应直接写 `^*`；改用 `$N^{*}$` 显式分组。全文检索确认仓库内无其他 `\*` 残留。
- 提交：`5e41a04 fix(bao2026-raw-rag)`。

### 2026-11-02 精读 RAW-RAG

- 归档：`papers/2610.30755v1.pdf` → `papers/bao2026-raw-rag/paper.pdf`；`paper-id` 取第一作者姓 `bao` + 年份 + `raw-rag`。提取全文（62 页），按 WWH-v6 产出 `notes/bao2026-raw-rag.md`（status: done）。
- 判型：实证与基准类为主，附少量系统与算法类；核心贡献是用一条配好的原始历史检索基线重设参照系，不是新记忆架构。
- 主结果（可在 Table 3 / Table 4 复核）：RAW-RAG 在 7 个基准-模型设置里 6 个第一，领先 0.13–5.53；唯一败场是 MEME + DeepSeek-V4-Flash，落后 MemMachine 1.52；补测 PersonaMem-v2 排第三（49.62，低于 MemOS 50.72、EverMemOS 53.25），正文未强调。
- 机制诊断：覆盖率跨度 26.22pp（MemoryAgentBench）/ 40.66pp（MEME），利用率只 9.71pp / 21.04pp；路径条件覆盖 RAW 62.34% 对 MemU 9.62%；完备存储的原始控制 61.60%，各系统低 4.06–30.54。
- 原文疑点（已写入 Ideas）：主表无置信区间，而 0.13 / 0.95 的领先贴着重跑噪声（LoCoMo 1,499 道未变题贡献 +0.281 分）；5k 对照对 RAW 不截、对 EverMemOS / MemMachine 各截 2,011 / 2,030 题；变异审计只测 Mem0；原子事实消融与 TTL 演示格式耦合；C/R 同时改了选择、打包与读者策略。
- 交叉引用：与 `he2026-memory-tax` 同题异路（一个造强 RAG，一个用收益/税账本），结论同向；`jiang2026-jev-mem` 的对比表缺 RAG，正是本文 Appendix E 批评的写法。
- 提交：`5362c45`（笔记）、`3a99777`（索引）、本文件随 `docs(status)`。

### 2026-11-02 精读 Memory Tax

- 新论文归档：PDF 原名为 `2610.34073v1.pdf`，误放在 `papers/jiang2026-jev-mem/` 下，已移至 `papers/he2026-memory-tax/paper.pdf`。`paper-id` 取第一作者姓 `he` + 年份 + `memory-tax`。
- 提取全文（36 页），按 WWH-v6 产出 `notes/he2026-memory-tax.md`（status: done）。
- 判型：实证与基准类为主，附少量系统算法类；核心贡献是"benefit / tax"的成对测量与四维归因，而非新记忆系统。
- 关键数字（均可在 Table 1 / Table 4 / Table 2 / Fig. 7 复核）：99 个系统-基准-主干格子里 90 个低于 RAG（2 轮），平均低 6.7 分，最大领先 +3.9、最大落后 −40.4；LongMemEval-s 上 SimpleMem / MemoryOS / Mem-T 的 tax 为 12.0 / 11.4 / 10.8；OpenViking 抽样事实只有 39.4% 完整保留、38.0% 无对应单元。
- 原文疑点（已写入笔记 Ideas，未回改原文）：§4.1 未给 tax 公式，公式为按 Table 4 反推并三例验算；Table 4 与 Fig. 13 的 tax 数值不一致（SimpleMem 12.0 vs 15.0，MemoryOS 11.4 vs 12.8）；§6.2 称 recursive "validate its effectiveness"，但三例仅 +0.1 / +0.9 / +3.6，其中 SimpleMem 的 tax 反而升高；MINT-Eval 上 Retrieval Scope 从 5.93% 到 31.87%，未真正对齐。
- 交叉引用：本文评测的 MAGMA 与仓库已有 `jiang2026-jev-mem` 同作者组，且是后者的主基线；后者的对比表中没有 RAG，正是本文 §B.2 批评的写法。
- 新增概念笔记 `notes/concepts/agent-memory-basics.md`：解释"跨会话""外面挂一层记忆"这类被压缩的背景概念，含写入/读取流程图与三种记忆存放位置的对照表。论文笔记 Why 首句改为指向它，不再把解释压回正文。
- 新增概念笔记 `notes/concepts/memory-pipeline.md`：逐条解释 Why 里的"五道工序"（抽事实、摘要、连图、分层、学习式策略），每道工序写清输入、产出、买到的收益、赔掉的代价，并用"花生过敏"的例子把五道工序串一遍；末尾给出"工序 → 损失形态 → 论文证据"的对应表（已注明是整理而非原文结论），以及四个评测分组与工序的关系。论文笔记 Why 第二句同步指向它。
- 提交：`6a57f52`（笔记）、`34f60fd`（概念笔记）、`e789a4b`（索引）、`09798cf`（状态）。

### 2026-10-29 修正记忆结构的表述

- 原句"四种关系都指向同一批记忆"中"指向"含义不明，且容易被读成"一条记忆有四个属性"。
- 改为节点与边的说法：记忆是节点，带内容、时间戳、来源、实体、向量；语义、时间、因果、实体是节点之间的四类边，同一对记忆可同时有多条不同类型的边；实体既是字段也可生成边。
- Mermaid 记忆库改为两条记忆节点 + 四条带标签的边，图注同步说明；What 中同一说法一并修正。

### 2026-10-29 统一元信息格式

- front matter 改为块状列表：`tags`、`aliases` 每行一项；新增 `aliases` 存放中文名与常用缩写。
- 笔记 `jiang2026-jev-mem.md` 同步；`AGENTS.md` 模板与说明、`WWH.md` 产出契约一并更新，并修正 `WWH.md` 里遗留的 v3 版本引用。

### 2026-10-29 重写 How

- 诊断：符号先于解释、单条塞四五个专名与阈值、全节没有一次完整流程示例；证据部分整表重述 What 的数字。
- 改写：合并"判型"到开场；新增"一、那个只打分的模型"；写入与查找改为六步叙述，参数放进句子；新写"四、走一遍"（附录 B 的自行车例子，注明虚构与分数非实测）；证据节只谈"能证明什么、不能证明什么"；开销节补三类失效条件。
- 公式：五路信号逐条说明来源与含义，给出读法与"权重都取 0.2"的假设示例，标出 λ 未给与重复归一问题；时效修正逐符号解释 ρ、r(q)、0.1 与分母的作用，并区分观测时间与事件时间。
- 插图：删除两张 PDF 截图，改用 Mermaid 重画总体闭环与系统结构；`AGENTS.md` 第 3 节新增"结构类图优先 Mermaid"规则。

### 2026-10-29 WWH 升到 v6：段落形态与四段边界

- 起因：v5 被机械执行成"一句话一段"，排版散乱；What 里的四条"新方法"实际在讲机制，与 How 重复。
- `WWH.md`：段落规则改为"一段讲一个意思、3–6 句、句间有承接，禁止一句一段"；职责表写明 What 不写步骤/公式/参数、How 不重复结论与数字；第 5、6 节各加一条边界判据。
- 笔记：What 开头合成两段；两个"新认识"、四个"新方法"、四条"新结论"改为有承接的段落；机制细节（判断格式、预算分配、写入不取舍）只保留结论层面的描述，执行细节交给 How；How 补上"写入不做取舍"的说明。

### 2026-10-29 WWH 升到 v5：段落密度

- 起因：What 虽然内容对，但一段里塞了四五个意思，读者仍要反复回读。
- `WWH.md` 第 8 节新增第 9 条：一段只放一个意思、通常 2–4 句，出现第二个"但是/同时/因此"即拆段；带加粗小标题的条目把做法、例子、理由分三段写。产出契约同步。
- 笔记 What 按此重排：开头四类判断单独列表，做法与边界拆段；两个"新认识"、四个"新方法"、四条"新结论"全部改为"加粗结论 + 2–3 段短说明"。

### 2026-10-29 WWH 升到 v4：去掉 TL;DR，Why 与 What 分工

- 起因：What 与 Why 内容重复；`TL;DR` 这类小标题本身暗示压缩，是讲不清的来源。
- `WWH.md`：Why 只提出问题、不给解法，结尾停在一个待答问题上；What 从答案写起，取消 `TL;DR`/摘要式小标题，明确不得复述 Why 的动机与成本账；职责表与产出契约同步。
- 笔记：Why 结尾改为待答问题与两个验收条件；What 开头给出答案与效果/成本两组数字，三组结论改用小标题；Jev 的输入输出细节移入 How 的核心机制。

### 2026-10-29 WWH 升到 v3：撤销压缩式要求

- 起因：v2 的"每段首句一句人话"被执行成了压缩，一句话塞多个概念，读者读两三遍仍不知所云。
- `WWH.md` 第 8 节改为"讲完整优先"：先解释后命名、一句只放一个意思、该留的句子必须留；新增"压缩式"失败案例，与抄论文、讲清楚并列对照；篇幅不再设上限（Why 通常 600–900 字）。
- 产出契约与自检同步改为 v3 口径；`AGENTS.md` 模板与自检一并更新。
- 笔记 `jiang2026-jev-mem.md` 按 v3 重写：Why 改为完整背景叙述，TL;DR 分为三步，结论清单去掉 write/read 侧等缩写，Table 1 前增加"这张表在比什么"，Ideas 与可复现开头展开为完整疑问。

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
- 提取全文（16 页），裁剪 Fig. 1、Fig. 2 至 `notes/assets/jiang2026-jev-mem/`（后按仓库插图规则改用 Mermaid 重画，截图已删除）。
- 产出笔记（status: done），创建 `README.md` 索引。
- 记录原文疑点：§4.2 正文数字与 Table 1 不一致（Multi-Hop 0.625/0.623、Open-Domain 0.610/0.618、Single-Hop 0.797/0.802）；正文声称 Temporal 追平 0.650 但表中为 0.637；§4.1 称两个数据集但只报告 LoCoMo；无消融实验。

### 2026-10-29 仓库初始化

- 建立 `AGENTS.md`：仓库边界、相对路径、目录与命名、uv-only、笔记模板、提交规范。
- 初始化 git，默认分支 `main`；添加 `.gitignore`。
- 将论文 PDF 归档为 `papers/<paper-id>/paper.pdf`。
- 提交：`2a8bee1`（规则）；原文归档提交已在历史重写中移除。

## 下一步

- [ ] 核对 <https://github.com/boleima/ImperfectiveParadox> 是否放出人类逻辑标签、逐题输出、格式遵循率、BERT 层与池化细节；若放出，回填 `ma2026-imperfective-paradox` 的"可复现"与 Ideas 第一条、第二条。
- [ ] 向小米 LLM-Core 确认 HySparse2 是否放出模型权重/代码、AgentPPL 与 Repo Code PPL 的构造、prefill 延迟与 KV 传输数据；若放出，回填 `wei2026-hysparse2` 的"可复现"与 Ideas 第一条、第三条。
- [ ] 向 SRA 作者索取预处理脚本、R 模型代码与各语言词频来源；若放出，回填 `xu2025-sra` 的"可复现"与 Ideas 第一条、第二条。
- [ ] 核对 <https://github.com/thu-nics/C2C> 是否给出融合器逐层参数、训练数据与评测集去重、长上下文融合延迟、多种子结果；若放出，回填 `fu2025-c2c` 的"可复现"与 Ideas 第一条、第二条。
- [ ] 核对 <https://github.com/Sherlockwz/T-Mem> 是否给出 LoCoMo-Plus 题数与运行次数、reranker 配置、主题与触发器数量、增量更新脚本；若放出，回填 `guo2026-t-mem` 的"可复现"与 Ideas 第一条、第二条、第四条。
- [ ] 核对 <https://github.com/google-research/rrsi> 与 <https://regularized-rsi.com> 是否给出搜索成本账本、四个基线的实现与超参、逐条约束消融、judge 提示词；若放出，回填 `xia2026-rrsi` 的"可复现"与 Ideas 第二条、第三条。
- [ ] 核对 OneRec 是否放出代码、奖励模型结构、Pass@512 采样的延迟与成本口径；若放出，回填 `zhou2025-onerec` 的"可复现"与 Ideas 第三条（收益/税账本）。
- [ ] 核对 <https://github.com/wangshy31/OneRec-Think> 是否包含公开实验脚本、人工类别 CoT 模板、Think-Ahead 的 `T` / `m` 与延迟数据；若放出，回填 `liu2025-onerec-think` 的"可复现"与 Ideas 第一条、第五条。
- [ ] 向 OneReason 作者确认 RL 超参（`N` / `K` / `β` / 分阶段裁剪范围）、OneReason-Bench 题目是否公开、OneReason-8B 与 0.8B 权重与许可；确认后回填 `onerec2026-onereason` 的"可复现"与 Ideas 第六条。
- [ ] 核对 <https://github.com/Ayanami0730/arag> 是否给出最大迭代步数、语料规模与块数、逐题结果、判定器提示词；若放出，回填 `du2026-a-rag` 的"可复现"与 Ideas 第一条。
- [ ] 核对 <https://github.com/DCI-Agent/DCI-Agent-Lite> 是否给出 CC 的 harness 配置、50 题采样种子、每题成本明细、L3/L4 的主结果口径与答案泄漏防护；若放出，回填 `li2026-dci` 的"可复现"与 Ideas 第四条。
- [ ] 核对 <https://github.com/HughieHu/Sage> 是否放出 1,200 题、20 万篇语料、人工校验记录、关键词生成与索引构建的 GPU 小时/美元成本；若放出，回填 `hu2026-sage` 的"可复现"与 Ideas 第四条。
- [ ] 核对代码仓库 <https://github.com/libingzheren/Jev-Mem> 是否公开、是否给出第二数据集与消融。
- [ ] 若确认正文数字与表格冲突，追加 `fix(jiang2026-jev-mem)` 提交修正笔记措辞。
- [ ] 核对 <https://github.com/hexuan21/MemoryTax> 是否放出 tax 计算脚本，若放出则回填笔记中"公式为反推"的说明。
- [ ] 核对 <https://github.com/Litmeb/RAW-RAG> 是否放出 5k 重跑日志、完备存储导出与逐题置信区间；若放出，回填 `bao2026-raw-rag` 的"可复现"与 Ideas 第一条。
- [ ] 核对 <https://github.com/deeplearning-wisc/OAT> 是否放出成功轨迹隐状态、标注工具与 CORAL 五折数字；若放出，回填 `yeh2026-oat` 的"可复现"与 Ideas 第三条。
- [ ] 核对 DecisionRAG 是否放出代码、Jev 之外的判断器权重与层级构建脚本；若放出，回填 `wan2026-decision-rag` 的"可复现"，并确认 NQ 设计题用的是哪个划分。
- [ ] 核对 <https://github.com/simple-agent-lab/RSIHub> 是否放出 `archive.jsonl`、Table 1 的逐题结果与每格实际花费；若放出，回填 `wang2026-rsi-hub` 的"可复现"，并把同预算 best-of-$k$ 对照（Ideas 第二条）做成可复算。
- [ ] 查 Hyperagents 配方里可变面是否包含 Gate 与 Select；若包含，`wang2026-rsi-hub` Ideas 第四条从推测升级为已存在，并补一条 `notes` 说明。
- [ ] 向 OO-Harness 作者确认是否放出代码、三个基准的 discovery/held-out 划分种子、接受节点数与 acceptance checks；若放出，回填 `li2026-oo-harness` 的"可复现"与 Ideas 第六条。
- [ ] 核对 <https://github.com/meghanadhpulivarthi/stair-clean> 是否放出微调权重、随机种子与"生成标题如何匹配 gold 叶"的代码；若放出，回填 `kumar2026-stair` 的"可复现"与 Ideas 第二条。
- [ ] 向 STAIR 作者确认三件事：STAIR 是一套模型还是每本书一套；Mistral 与 Haiku 是否看到目录、是否用约束解码；0.05% 幻觉统计是否在约束解码下做的。确认后修正笔记 How 与 Ideas 第四条。
- [ ] 核对 <https://github.com/itsnamgyu/declarative-attention> 是否放出 21 个源的逐源题数、全 21 源宏平均、DSA 扫描插桩与非法 focus 回退；若放出，回填 `ho2026-declarative-attention` 的"可复现"与 Ideas 第一条。

## 阻塞 / 待确认

- `ma2026-imperfective-paradox` 的 Group C 金标签是理论语义学的 Unknown，人工评估只查语法/流利/充分，没有人类逻辑标注；引用 TBR/ΔAA 时需注明这是"相对理论标签"的偏置。
- `wei2026-hysparse2` 的主对比同时改了头配置（MQA 64/1/256 vs GQA 64/4/192/128），KV-Cache 与效率收益不能全部归给两级 KV 共享；引用 2.69 GB / 2.92× 时需注明。
- `xu2025-sra` 的词频控制用英语 norms 覆盖 10 种语言，非英语语言的词频控制不可靠；引用跨语言结论时需注明。
- `xu2025-sra` 的 6/10 正效应与 4/10 负效应不能写成"普遍规律"；引用时需注明。
- `fu2025-c2c` 的"2.5× average speedup"口径未定：Table 4 三组是 3.46× / 1.51× / 14.41×，算术平均 6.46×；引用加速比时需注明是单组还是平均。
- `fu2025-c2c` 的 300 步检查点 MMLU-Redux 44.30 高于最终检查点 42.92，主表用最终检查点；引用 42.92 时需注明这不是训练过程中最好的检查点。
- `guo2026-t-mem` 的 LoCoMo 与 LoCoMo-Plus 使用不同答题/评判协议（GPT-4o-mini vs GPT-4o + Gemini-2.5-Flash），5.45 的 gap 含协议差；引用时需注明。
- `xia2026-rrsi` 的"up to 4.3 points on the five OOD benchmarks"与 JobBench +4.7 冲突；摘要的 4.3 可能只指 Frontier-Eng，引用时需注明。
- `xia2026-rrsi` 的"30% fewer policy tokens"按 Table 2 是 36.3%（2.42 对 3.80）；引用时需注明。
- 历史已于 2026-11-04 重写以移除 PDF 并强推，旧 hash 全部失效；`backup/pre-pdf-rewrite` 仅存于本地，未推送。
- `du2026-a-rag` 的"3/5 数据集最好"口径未定：按 benchmark 数是 3 个（MuSiQue、HotpotQA、GraphRAG-Bench），按五个子集数是 4 个；引用主表时需注明。
- `du2026-a-rag` 的 §5.1 写 GPT-5 的扩展结果，Limitations 又说没有在 GPT-5 上验证；引用 +25% 时需注明该冲突。
- `li2026-dci` 的 DCI-Agent-CC 与检索基线不是同一 harness，多跳 QA 的最强基线还是 14B 开源模型；+11.0 与 +30.7 不能全部归因于接口，同模型同预算对照未做。
- `hu2026-sage` 的"BM25 高约 30%"是短答案、top-10、相对 gte-Qwen 的百分比（81.2 对 63.0）；开放式题 BM25 并不领先。稠密检索只编码前 32K token，BM25 索引全文，差距含覆盖率不对称。
- `bao2026-raw-rag` 主表沿用各基线原论文分数，未在同一次受控运行中重跑；要检验"0.13 分领先"这类结论，需等作者放出统一重跑或自行复现，笔记已按"主表无置信区间"记录，不据此改写结论。
- `AGENTS.md` 第 1 节目录树未收录 `notes/concepts/`，是否写进规则待决定。
- `yeh2026-oat` 的域外主结果使用全量 CORAL（含被评测轨迹的表示），五折版本只有图；引用 +7 点结论时需注明该口径。
- `li2026-oo-harness` 的路由模型口径未定：主文 §4.1 写 Sonnet 5，附录 A.4.2 默认 selection 为 Opus 4.8，Table 3 案例两者都用 Opus 4.8；引用主表数字时需注明该冲突。
- `kumar2026-stair` 的两个基线口径未定：正文只写 Mistral 用 beam search、Haiku 只出现在 Table 4 注里，都没写是否给目录、是否约束解码；Table 3 示例 1 的 Mistral 输出带完整编号，暗示它看到了目录，但无法确认。引用 13.8% 与 45.6% 时需注明。
- `kumar2026-stair` 的 STAIR 训练范围未定（一套模型覆盖 18 本书 vs 每本书一套），这直接决定成本与"知识入库"的解释；笔记按两种可能并列写，不采信其中一种。
- `ho2026-declarative-attention` 的 45.8%/1.40pp 是 15 个选定源上的数；另 6 个失败源只有 Gemma-4-31B 单次运行。笔记的"全 21 源"估计（-3.58pp、省 11.6%）是按每源等权换算的估计，不是论文数，引用时需注明口径。
- `ho2026-declarative-attention` 的非法 focus 回退策略、提示词开发集划分、每源过滤后题数均未写；DSA 的 indexer 扫描数是从生成结果重建的，不是插桩 kernel；这些缺口已写入笔记"可复现"，核对代码仓库后再补。
- `onerec2026-onereason` 的 `paper-id` 未按"第一作者姓"命名：论文署名是 `OneRec Team`，作者表明确按名字字母序排列，没有第一作者；暂用团队名，待用户确认是否改成 `yang2026-onereason`（Biao Yang 是字母序第一位，但不是第一作者）。
- `zhou2025-onerec` 的线上数字口径：A/B 的实验组是 5% 流量，OneRec 只替换该组内 25% 的降级（缓存）流量；引用 +0.54% / +1.24% 时必须注明"相对缓存结果"，不能写成"相对全量实时推荐"。
- `liu2025-onerec-think` 的公开基准口径：§A.1 说明公开数据用人工构造的类别 CoT 当激活内容，不是 §4.2 的自生成理由；引用 Table 1 / Table 2 时需注明这是"对齐 + 人工 CoT + SFT"，Table 1 是否包含 RL 也未写明。
- `onerec2026-onereason` 的"thinking 稳定优于非-thinking"只在 RFT 合并后的 R3 高 K 上成立：R0 的 token grounding 是 1.35 对 5.24，RFT 的 Cross-Video R@8 是 0.05 对 0.06；引用该结论时需带上条件。
