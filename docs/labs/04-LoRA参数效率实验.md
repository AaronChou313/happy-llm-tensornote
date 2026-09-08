---
id: lora-lab
title: LoRA 参数效率实验
section: 实验 / 模型训练
order: 650
tags: [lora, peft, matrix, lab]
aliases: [LoRA Lab]
prerequisites: [llm-training-practice]
summary: 通过参数计数和低秩矩阵乘法理解 LoRA 为何能减少可训练参数。
status: stable
---

# LoRA 参数效率实验

## 实验目标

对一个 $d_{out}\times d_{in}$ 权重矩阵，LoRA 不直接训练完整更新，而是学习两个更小矩阵的乘积 $BA$。

```python exec lab="lora-parameter-efficiency" cell="1" title="Compare parameter counts" difficulty="basic"
d_in = 4096
d_out = 4096
rank = 8

full_parameters = d_out * d_in
lora_parameters = rank * d_in + d_out * rank
ratio = lora_parameters / full_parameters

print({
    "full_update": full_parameters,
    "lora_update": lora_parameters,
    "trainable_ratio": f"{ratio:.3%}",
})
assert lora_parameters < full_parameters
```

```python exec lab="lora-parameter-efficiency" cell="2" title="Build a low rank update" difficulty="basic"
A = [[1.0, 0.0, -1.0], [0.0, 1.0, 1.0]]      # rank x d_in
B = [[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]]     # d_out x rank

delta = [
    [sum(B[row][inner] * A[inner][column] for inner in range(len(A)))
     for column in range(len(A[0]))]
    for row in range(len(B))
]

print("delta W:")
for row in delta:
    print(row)
assert len(delta) == len(B)
assert len(delta[0]) == len(A[0])
```

```python exec lab="lora-parameter-efficiency" cell="3" title="Explore rank tradeoffs" difficulty="basic"
for candidate_rank in (1, 4, 8, 16, 64):
    count = candidate_rank * d_in + d_out * candidate_rank
    print(candidate_rank, f"{count / full_parameters:.3%}")
```

## 复盘

- Rank 增大时，可训练参数量和更新表达能力如何变化？
- 参数更少为什么不等于训练显存按相同比例下降？
- 回到 [[llm-training-practice|第六章]]，定位 LoRA 被注入哪些线性层。
