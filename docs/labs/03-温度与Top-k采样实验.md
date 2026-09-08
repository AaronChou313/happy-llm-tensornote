---
id: sampling-lab
title: 温度与 Top-k 采样实验
section: 实验 / 生成
order: 410
tags: [generation, sampling, temperature, top-k]
aliases: [Sampling Lab]
prerequisites: [large-language-models]
summary: 观察温度和 Top-k 如何改变同一组 Logits 的概率集中程度与候选集合。
status: stable
---

# 温度与 Top-k 采样实验

## 实验目标

生成策略不会改变模型已经计算出的 Logits，却会改变我们从这些分数构造的采样分布。

```python exec lab="temperature-top-k" cell="1" title="Define logits and softmax" difficulty="basic"
from math import exp

tokens = ["模型", "学习", "生成", "训练", "注意力"]
logits = [3.2, 2.4, 1.8, 1.0, 0.6]

def probabilities(values, temperature=1.0):
    scaled = [value / temperature for value in values]
    peak = max(scaled)
    weights = [exp(value - peak) for value in scaled]
    total = sum(weights)
    return [weight / total for weight in weights]

assert len(tokens) == len(logits)
```

```python exec lab="temperature-top-k" cell="2" title="Compare temperatures" difficulty="basic"
for temperature in (0.5, 1.0, 2.0):
    probs = probabilities(logits, temperature)
    print(temperature, {token: round(prob, 4) for token, prob in zip(tokens, probs)})

cold = probabilities(logits, 0.5)
hot = probabilities(logits, 2.0)
assert max(cold) > max(hot)
```

```python exec lab="temperature-top-k" cell="3" title="Apply top k filtering" difficulty="basic"
k = 3
ranked_indices = sorted(range(len(logits)), key=logits.__getitem__, reverse=True)
kept = set(ranked_indices[:k])
filtered_tokens = [tokens[index] for index in ranked_indices[:k]]
filtered_logits = [logits[index] for index in ranked_indices[:k]]
filtered_probs = probabilities(filtered_logits, temperature=1.0)

print("kept:", filtered_tokens)
print("renormalized:", [round(prob, 4) for prob in filtered_probs])
assert len(kept) == k
assert abs(sum(filtered_probs) - 1.0) < 1e-12
```

## 复盘

- 温度趋近于零时，分布接近哪种解码策略？
- Top-k 为什么既可能减少离题，也可能删掉正确但低概率的候选？
- 继续阅读 [[large-language-models|第四章]]，区分模型能力和解码策略带来的行为差异。
