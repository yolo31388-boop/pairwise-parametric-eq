# pairwise-parametric-eq

## 领域

游戏、图形与多媒体

## 主题

参数均衡器级联

## 说明

系数状态同锁、跨块续接与增益统一。

初始状态下 `media/parametric_eq.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
