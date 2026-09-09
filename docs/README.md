---
id: happy-llm-course-home
title: Happy-LLM TensorNote 学习主页
section: 课程导航
order: 0
tags: [llm, course, roadmap, tensornote]
aliases: [Happy-LLM, 课程主页]
prerequisites: []
summary: 按“阅读、预测、实验、复盘”的节奏，从 NLP 基础逐步完成 LLM 与 Agentic RL 学习路径。
status: growing
source: https://github.com/datawhalechina/happy-llm
---

# Happy-LLM TensorNote 学习主页

![Happy-LLM 课程封面](./images/head.jpg)

本仓库是 [Happy-LLM](https://github.com/datawhalechina/happy-llm) 的 TensorNote 学习版。原教程内容和配套工程代码被保留；新增的知识导航、属性、WikiLinks、轻量 Lab 与章节级 Experiment，让你可以一边读，一边验证刚学到的概念。

> [!important]
> 文中原有的普通 `python` Fence 仍是讲解代码，不会自动执行。带完整 `python exec` 元数据的是共享 Kernel 的轻量 Lab；第五至第八章还提供 `tensornote-experiment` 项目实验面板，用于按预设准备依赖并运行多文件流程。

## 你将完成什么

- 建立从文本表示、注意力、预训练到大语言模型的概念链路。
- 理解 LLaMA 风格模型的关键组件，以及预训练、SFT、PEFT 的工程流程。
- 认识评测、RAG、Agent 与 Agentic RL 的问题设定。
- 通过小规模、确定性的 CPU 实验检查关键直觉，再决定是否运行章节中的重型工程代码。

## 推荐学习路径

| 阶段 | 先读 | 再做 | 完成标志 |
| --- | --- | --- | --- |
| 准备 | [[learning-environment|学习与环境准备]]、[[preface|前言]] | [[lab-workbench|实验工作台]] | 知道普通代码与 Lab 的区别 |
| 基础 | [[nlp-foundations|第一章 NLP 基础概念]] | [[tokenization-lab|文本切分与词表实验]] | 能解释表示粒度与未知词问题 |
| 架构 | [[transformer-architecture|第二章 Transformer 架构]] | [[attention-lab|缩放点积注意力实验]] | 能追踪 Query、Key、Value 的形状和权重 |
| 模型 | [[pretrained-language-models|第三章 预训练语言模型]]、[[large-language-models|第四章 大语言模型]] | [[sampling-lab|温度与 Top-k 采样实验]] | 能区分架构选择、训练目标与生成策略 |
| 构建 | [[build-an-llm|第五章 动手搭建大模型]] | Experiment：工程检查 → Tokenizer → 训练/导出 | 能从 Tokenizer 追踪到损失函数 |
| 训练 | [[llm-training-practice|第六章 大模型训练流程实践]] | Experiment：Notebook → 单卡/双卡 Pretrain 与 SFT | 能判断全参微调与 PEFT 的成本边界 |
| 应用 | [[llm-applications|第七章 大模型应用]] | Experiment：离线 RAG/Agent → API 完整流程 | 能描述检索、生成与工具调用的数据流 |
| 强化学习 | [[llm-reinforcement-learning|第八章 大模型强化学习]] | [[grpo-lab|组内相对优势实验]] → Agentic RL Experiment | 能解释组内标准化如何产生相对优势 |
| 拓展 | [[extra-chapter-home|拓展专题]] | 按兴趣选择社区文章与配套工程 | 能把专题放回主线知识图谱中理解 |

## 在 TensorNote 中学习

1. 从本页进入一章，先读 Frontmatter 中的摘要和先修关系。
2. 遇到公式或代码前，先写下你对输出形状、数值趋势或失败条件的预测。
3. 轻量概念实验打开对应 Lab，连接自己的 Jupyter Kernel 后使用 **Restart & Run All**。
4. 第五至第八章先运行默认离线 smoke，再审阅 Experiment 计划、依赖、下载、算力和费用，按需显式启动完整预设。
5. 对照观察结果，在章节末的复盘问题中记录仍不确定的地方。

> [!pitfall]
> `features.executable: true` 只表示本仓库有意提供 Lab，并不等于自动授权运行。你仍需在 TensorNote 中审阅代码、允许当前 Workspace 执行，并连接可访问的 Jupyter Kernel；GitHub Workspace 还需要信任当前提交。

## 通过 GitHub 打开

仓库发布为公开 GitHub Repository 后，在 TensorNote 的 **Open Workspace → GitHub** 中粘贴 [`https://github.com/AaronChou313/happy-llm-tensornote`](https://github.com/AaronChou313/happy-llm-tensornote) 即可。TensorNote 会从仓库根目录读取 `tensornote.yaml`，以本页作为默认笔记，并按 `docs/` 下的文件结构构建导航。

GitHub Workspace 默认只读；阅读、搜索、WikiLink 和属性浏览不需要本地服务。运行 Lab 时，读者还需信任当前 `owner/repository@commitSHA`、允许执行，并连接自己的 Jupyter Compute Profile。仓库更新到新提交后，执行信任需要重新确认。

## 两种实践强度

### 轻量概念实验

`docs/labs/` 中的 Lab 只使用 Python 标准库，数据规模很小，不联网、不下载模型，适合边读边验证。

### 完整章节工程

第五至第八章包含模型下载、GPU 训练、分布式训练、外部服务或额外依赖。每章正文顶部都有项目 Experiment：默认预设是离线、确定、可重复的 smoke；完整流程拆成独立依赖环境和显式预设。请先阅读 [[learning-environment|学习与环境准备]]，审阅运行计划后再启动。API 密钥只放在 TensorNote 的受信任运行环境；第八章远端训练可能产生费用，ReTool 必须在操作系统级隔离环境运行。

## 学习进度

- [ ] 完成环境与 TensorNote 执行权限检查
- [ ] 第一章：NLP 基础与文本表示
- [ ] 第二章：Transformer 与注意力
- [ ] 第三、四章：预训练模型与 LLM
- [ ] 第五章：手写 LLaMA 风格模型
- [ ] 第六章：预训练、SFT 与 PEFT
- [ ] 第七章：评测、RAG 与 Agent
- [ ] 第八章：Agentic RL
- [ ] 按兴趣完成至少一个拓展专题

## 来源与许可

课程正文源自 Datawhale Happy-LLM，继续遵循仓库根目录中的许可协议。TensorNote 适配层只改变学习组织和实验体验，不改变原作者署名与正文来源。
