# 论文精读

精读笔记在 `notes/<paper-id>.md`，分类信息写在笔记的 `tags` 里，不建分类目录。论文原文只保留在本地 `papers/<paper-id>/paper.pdf`，不入库；clone 后按下方索引里的 arXiv 链接自行下载。

所有笔记遵循 [`WWH.md`](WWH.md) 阅读模型：**Why → What → How → Ideas**。每篇笔记的 front matter 用 `model:` 记录所依据的模型版本，方便日后按版本演进回填。

## 索引

按 `paper-id` 倒序排列。

| paper-id | 标题 | 年份 | arxiv | tags | status |
| --- | --- | --- | --- | --- | --- |
| [cardei2026-irah](notes/cardei2026-irah.md) | IRAH: Hierarchical Agentic Tree Search for Retrieval Pipeline Optimization | 2026 | [2610.30167](https://arxiv.org/abs/2610.30167) | retrieval-augmented-generation, retrieval-pipeline, hyperparameter-optimization, tree-search, monte-carlo-tree-search, meta-learning, warm-start | done |
| [hazoom2026-factual-nuggets](notes/hazoom2026-factual-nuggets.md) | Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG | 2026 | [2605.25641](https://arxiv.org/abs/2605.25641) | retrieval-augmented-generation, agentic-rag, knowledge-base-curation, document-expansion, feedback-learning, production-deployment, discoverability | done |
| [cadet2026-workflow-mining](notes/cadet2026-workflow-mining.md) | Mining the Design Space of Multi-Agent Workflows | 2026 | [2610.31709](https://arxiv.org/abs/2610.31709) | multi-agent-systems, workflow-design, design-space-mining, monte-carlo-tree-search, feature-mining, empirical-study, prompt-structure | done |
| [li2026-thinkingbox](notes/li2026-thinkingbox.md) | One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows | 2026 | [2608.19741](https://arxiv.org/abs/2608.19741) | agent-benchmark, stateful-workflow, tool-use, reliability, pass-at-k, side-effect-verification, reinforcement-learning, enterprise | done |
| [schneider2026-lakehouse-skills](notes/schneider2026-lakehouse-skills.md) | "Skill Issues": Data-Centric Optimization of Lakehouse Agents | 2026 | [2606.01185](https://arxiv.org/abs/2606.01185) | agent-skills, data-agents, lakehouse, state-verification, prompt-optimization, gepa, benchmark-generation | done |
| [wu2026-longmemeval-v2](notes/wu2026-longmemeval-v2.md) | LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues | 2026 | [2605.12493](https://arxiv.org/abs/2605.12493) | agent-memory, benchmark, long-term-memory, web-agents, context-gathering, coding-agent-as-memory, evidence-selection | done |
| [pysklo2026-agent-diff](notes/pysklo2026-agent-diff.md) | Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation | 2026 | [2602.11224](https://arxiv.org/abs/2602.11224) | agent-benchmark, enterprise-saas, api-replication, state-diff, closed-world-invariant, code-execution, side-effect-verification | done |
| [ma2026-imperfective-paradox](notes/ma2026-imperfective-paradox.md) | The Imperfective Paradox in Large Language Models | 2026 | [2601.09373](https://arxiv.org/abs/2601.09373) | semantics, aspect, natural-language-inference, llm-reasoning, teleological-bias, diagnostic-dataset | done |
| [wei2026-hysparse2](notes/wei2026-hysparse2.md) | HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing | 2026 | [2609.26368](https://arxiv.org/abs/2609.26368) | long-context, sparse-attention, kv-cache, kv-sharing, prefill-efficiency, mixture-of-experts | done |
| [xu2025-sra](notes/xu2025-sra.md) | Strategic resource allocation in memory encoding: An efficiency principle shaping language processing | 2025 | [2503.14728](https://arxiv.org/abs/2503.14728) | psycholinguistics, working-memory, resource-rational, dependency-locality, surprisal, cross-linguistic | done |
| [fu2025-c2c](notes/fu2025-c2c.md) | Cache-to-Cache: Direct Semantic Communication Between Large Language Models | 2025 | [2510.03215](https://arxiv.org/abs/2510.03215) | multi-llm, kv-cache, cross-model-communication, latent-communication, inference-efficiency, model-fusion | done |
| [guo2026-t-mem](notes/guo2026-t-mem.md) | T-Mem: Memory That Anticipates, Not Archives | 2026 | [2606.15405](https://arxiv.org/abs/2606.15405) | agent-memory, long-term-memory, associative-recall, retrieval, write-time-indexing, locomo, llm-as-judge | done |
| [xia2026-rrsi](notes/xia2026-rrsi.md) | RRSI: Regularized Recursive Self-Improvement of Agent Harnesses | 2026 | [2609.24972](https://arxiv.org/abs/2609.24972) | agent-harness, self-improvement, recursive-self-improvement, overfitting, regularization, agent-evolution, benchmark-transfer | done |
| [zhou2025-onerec](notes/zhou2025-onerec.md) | OneRec Technical Report | 2025 | [2506.13695](https://arxiv.org/abs/2506.13695) | generative-recommendation, semantic-id, industrial-deployment, reinforcement-learning, scaling-law, system-design | done |
| [liu2025-onerec-think](notes/liu2025-onerec-think.md) | OneRec-Think: In-Text Reasoning for Generative Recommendation | 2025 | [2510.11639](https://arxiv.org/abs/2510.11639) | generative-recommendation, chain-of-thought, reasoning, itemic-token, reinforcement-learning, industrial-deployment | done |
| [onerec2026-onereason](notes/onerec2026-onereason.md) | OneReason Technical Report | 2026 | [2606.06260](https://arxiv.org/abs/2606.06260) | generative-recommendation, reasoning, chain-of-thought, reinforcement-learning, benchmark, distillation, industrial-deployment | done |
| [hu2026-sage](notes/hu2026-sage.md) | SAGE: Benchmarking and Improving Retrieval for Deep Research Agents | 2026 | [2602.05975](https://arxiv.org/abs/2602.05975) | deep-research, agentic-retrieval, benchmark, scientific-literature, sparse-retrieval, dense-retrieval, test-time-scaling | done |
| [li2026-dci](notes/li2026-dci.md) | Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction | 2026 | [2605.05242](https://arxiv.org/abs/2605.05242) | retrieval, agentic-search, direct-corpus-interaction, terminal-tools, retrieval-interface, multi-hop-qa, information-retrieval | done |
| [du2026-a-rag](notes/du2026-a-rag.md) | A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces | 2026 | [2602.03442](https://arxiv.org/abs/2602.03442) | retrieval-augmented-generation, agentic-rag, tool-use, hierarchical-retrieval, multi-hop-qa, context-efficiency, test-time-scaling | done |
| [ho2026-declarative-attention](notes/ho2026-declarative-attention.md) | Language Models Can Control Their Own Attention | 2026 | [2609.02737](https://arxiv.org/abs/2609.02737) | long-context, sparse-attention, kv-cache, decoding, chain-of-thought, inference-efficiency, prompt-protocol | done |
| [kumar2026-stair](notes/kumar2026-stair.md) | STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation | 2026 | [2609.03874](https://arxiv.org/abs/2609.03874) | retrieval, retrieval-augmented-generation, document-structure, table-of-contents, model-based-indexing, benchmark | done |
| [yeh2026-oat](notes/yeh2026-oat.md) | Tracing Agentic Failure from the Flow of Success | 2026 | [2607.12747](https://arxiv.org/abs/2607.12747) | agent-failure-attribution, anomaly-detection, one-class-learning, neural-cde, agent-debugging | done |
| [wang2026-rsi-hub](notes/wang2026-rsi-hub.md) | RSIHub: A Composable Framework for Agent-Evolution Methods | 2026 | [2610.32253](https://arxiv.org/abs/2610.32253) | agent-evolution, self-improving-agents, agent-harness, framework, provenance, evaluation-protocol | done |
| [wan2026-decision-rag](notes/wan2026-decision-rag.md) | Retriever-Free Retrieval: Navigating Documents with Decision Models | 2026 | [2610.35868](https://arxiv.org/abs/2610.35868) | retrieval, retrieval-augmented-generation, decision-models, hierarchical-retrieval, efficiency | done |
| [li2026-oo-harness](notes/li2026-oo-harness.md) | Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design | 2026 | [2610.28380](https://arxiv.org/abs/2610.28380) | agent-harness, self-evolving-agents, code-evolution, object-oriented-design, task-routing, long-horizon-agents | done |
| [jiang2026-jev-mem](notes/jiang2026-jev-mem.md) | Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents | 2026 | [2609.23986](https://arxiv.org/abs/2609.23986) | agent-memory, memory-control, multi-relational-graph, adaptive-retrieval, efficiency, locomo | done |
| [he2026-memory-tax](notes/he2026-memory-tax.md) | Memory Tax: Dissecting the Net Value of Agent Memory | 2026 | [2610.34073](https://arxiv.org/abs/2610.34073) | agent-memory, evaluation, benchmark, memory-tax, retrieval-augmented-generation, cost-analysis | done |
| [bao2026-raw-rag](notes/bao2026-raw-rag.md) | Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought | 2026 | [2610.30755](https://arxiv.org/abs/2610.30755) | agent-memory, evaluation, retrieval-augmented-generation, long-term-memory, evidence-coverage, cost-analysis | done |

概念说明不对应单篇论文，放在 `notes/concepts/`，不计入上表：[长期记忆：为什么要在模型外面挂一层](notes/concepts/agent-memory-basics.md)、[记忆流水线：五道工序与它们的代价](notes/concepts/memory-pipeline.md)、[失败归因：为什么最后一步看不到病因](notes/concepts/failure-attribution.md)、[智能体进化：把执行反馈变成持久修改](notes/concepts/agent-evolution.md)、[稠密检索：文本怎么变成向量，什么被保留、什么被丢掉](notes/concepts/dense-retrieval.md)、[先验概率：看证据之前，你信什么](notes/concepts/prior-probability.md)。

## 工作流

见 `AGENTS.md`；当前进度见 `STATUS.md`。先把原文下载到 `papers/<paper-id>/paper.pdf`（仅本地），再解析：

```bash
uv run tools/pdf_extract.py papers/<paper-id>/paper.pdf
```
