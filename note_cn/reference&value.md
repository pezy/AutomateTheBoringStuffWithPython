# 引用与值

几乎在任何语言里, 这两者的区分都是组最基础的重点.

Python 里的区别不露痕迹, 对于 `x = y` 这样的式子, x 到底是引用, 还是值, 完全取决于 y 的类型. 如果 y 是字符串, 数值, 元组这种**不可变类型**, x 就是值. 而如果 y 是列表, 字典这样的**可变类型**而言, x 就是引用.

对于列表而言, 如果你想要 copy 值, 就需要显式的调用 `copy()` 方法, 如果要更彻底一些, 连 list 里包含的子 list 也要一起 copy, 那么则需要用到 `deepcopy()` 方法.