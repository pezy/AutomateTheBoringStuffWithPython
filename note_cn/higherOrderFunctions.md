# 高阶函数

在编程语言中, 我们会将一些常用的操作步骤封装起来, 给它个名字. 下次需要用到该操作时, 只需要通过这个名字来调用即可. 这种特性我们称之为函数, 其作为一种基本的抽象手段, 可以将我们从繁琐细碎的低层面操作中解脱出来.

为了让这种抽象手段更加通用, 函数的参数应该也可以是一个函数, 函数的返回值, 也可以是一个函数. 这种参数与返回值涉及到其他函数的函数, 我们就称之为**高阶函数**, 也被称之为**函子**.

高阶函数要比函数更加强悍, 极大程度上增强了编程语言的表现力.

### 函数作为参数

首先, 我们来看一下最简单的一个自然数求和函数:

```python
def sum_naturals(n):
    total, k = 0, 1;
    while k <= n:
        total, k = total + k, k + 1
    return total
```

然后, 需求有点变化, 让你计算立方根的和:

```python
def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total
```

接着, 需求又变了, 让你计算下图所示形式的和:

$$
\frac{8}{1\cdot3} + \frac{8}{5\cdot7} + \frac{8}{9\cdot11}+...
$$
这是一种慢速求解 PI 的方法.

```python
def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total
```

此时此刻, 想必你已经复制粘贴三次并修改代码了. 其实我们完全可以抽象出一个更加通用的模版:

```python
def <name>(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + <term>(k), k + 1
    return total
```

抽象出各种 term 的求和过程.

```python
# template (high-order functions)
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

# functions
def identity(x):
    return x

def cube(x):
    return x*x*x

def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

# refactoring
def sum_naturals(n):
    return summation(n, identity)

def sum_cubes(n):
    return summation(n, cube)

def pi_sum(n):
    return summation(n, pi_term)

# test
print(sum_naturals(10)) #55
print(sum_cubes(3)) #36
print(pi_sum(1e6)) #3.141592153589902
```

## 函数作为通用方法

我们计划实现一个**迭代改进**的抽象方法, 并用它来计算[黄金分割率](https://en.wikipedia.org/wiki/Golden_ratio)(通常称之为 "phi"). 我们假设 `guess` 作为方程的最终解, 然后用 `update` 来不断优化该解, 最终通过 `close` 来检测当前的 `guess` 是否足够接近正确值.

```python
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess
```

> 黄金分割率的基本公式
> $$
> \frac{a + b}{a} = \frac{a}{b} = \varphi
> $$
> 可以推导出:
> $$
> \frac{a+b}{a} = 1 + \frac{b}{a} = 1 + \frac{1}{\varphi} = \varphi
> $$
>
> $$
> \varphi + 1 = \varphi^2
> $$
>

于是我们的 `update` 过程就可以是不断的让 1 加上 guess 倒数的过程.

```python
def golden_update(guess):
    return 1/guess + 1
```

而验证其是否足够接近则可以判断 guess 的平方是否等于它自身加一.

```python
def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)
```

由于判断两个浮点数是否相等并不能通过一个等于号来搞定, 所以我们还需要引入一个函数:

```python
def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance
```

最后我们可以计算出 phi 来:

```python
>>> improve(golden_update, square_close_to_successor)
>>> 1.6180339887498951
```

**抽象**与**组合**是计算机科学中两个最重要的手段, 两者互相联系, 相辅相成. 好的命名与函数化, 就是非常具体的抽象手段, 让我们摆脱具体的计算方法, 把精力放在整理通用流程上. 而在 python 里, 我们又可以轻而易举的将小的模块(譬如`update`, `close` 等), 组合成复杂的流程(`improve`). 这就好比搭积木, 组合的过程, 也是对流程加强理解的过程.

最后我们将写一段测试程序, 来验证我们的通用逼近方法的正确性.

```python
from math import sqrt
phi = 1/2 + sqrt(5)/2 # phi's value.

def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

improve_test()
```

## 嵌套定义函数

上面的内容, 已经让我们丰富了编程语言的抽象能力. 但也带来了一个恼人的问题: 就是在全局栈中, 处处都是小函数的定义, 如果不加注释, 则显得过于杂乱无章, 给维护增添了麻烦. 而且函数的签名也成了束缚, 譬如 `update` 传入 `improve` 时, 就只能接受一个参数. 

运用嵌套定义, 就是为了解决上述这两个问题.

来看看一个新问题: 计算平方根(`sqrt`).

> 用牛顿法推导公式: (假设寻找 S 的平方根)
> $$
> f(x) = x^2 - S = 0
> $$
>
> $$
> x_{n+1} = x_{n} - \frac{f(x_n)}{f'(x_n)} = x_n - \frac{x^2_n - S}{2x_n} = \frac{1}{2}(x_n + \frac{S}{x_n})
> $$
>

```python
def average(x, y):
    return (x + y)/2
def sqrt_update(x, a):
    return average(x, a/x)
```

但我们发现问题来了. 这两个函数都是需要两个参数的. 我们既有的 `improve`已然不适用. 于是祭出嵌套定义.

```python
def sqrt(S):
    def sqrt_update(x):
        return average(x, S/x)
    def sqrt_close(x):
        return approx_eq(x * x, S)
    return improve(sqrt_update, sqrt_close)
```

这里就要介绍一下**域**的概念了. 我们之前写的函数, 都在全局域里, 但实际上函数自身在调用时, 也会开辟一段域. 如 `sqrt`内部, 就属于全局域的子域. 在 `sqrt_update` 内部, 就是 `sqrt` 的子域. **子域中, 可以够得着外域的变量, 反之却有问题.**

类似 `sqrt_update`这样, 够得着外域的变量(如`S`), 又躲在 `sqrt` 函数的内部, 不污染全局域. 我们将这样封装信息的手段, 称之为**闭包**.

## 函数作为返回值

假设我们需要定义这样一种函数:
$$
h(x) = f(g(x))
$$
可以这样嵌套:

```python
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
```

命名中的 `1` 代表着 `h`, `f`, `g`的参数, 以及返回值, 都是一个.

## 例子: 牛顿法

上面各类高阶函数的特性都介绍了一遍. 接下来, 我们通过一个具体的例子, 来看看它的威力.

[牛顿法](https://en.wikipedia.org/wiki/Newton%27s_method)是一种利用逼近法求根的经典方法, 刚才求平方根的数学推导就用到了它. 
$$
x : f(x) = 0.
$$
求解的逼近过程可以用下面这个式子来表达:
$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$
据此, 我们来提供 `newton_update`:

```python
def newton_update(f, df):
    def update(x):
        return x - f(x)/df(x)
    return update
```

以及通用求根的方法:

```python
def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)
```

这样, 我们重构一下用牛顿法求平方根的写法:

```python
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)
```

并且可以推广到 n 方根:

```python
def power(x, n):
    '''Return x * x * x * ... * x for x repeated n times.'''
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)
```

## 柯里化(Currying)

利用高阶函数, 我们可以将多参数的函数转换为单参数形式, 例如, 给定 `f(x, y)`, 我们可以定义 `g(x)(y)` 等价于 `f(x, y)`. 这里的 `g` 就是一个高阶函数. 这种转换, 被称为柯里化(Currying).

下面是柯里化版本的 `pow` 函数:

```python
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

>>> curried_pow(2)(3)
8
```

函数式编程中(尤其是 Haskell), 会规定函数只允许有一个参数. 所以这就要求程序员对多参数的情况进行柯里化. 譬如我们可以写这样一个函数来映射处理一系列值:

```python
def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1
        
map_to_range(0, 10, curried_pow(2))
1
2
4
8
16
32
64
128
256
512
```

对于上述例子, 我们要计算的都是以 2 为底的 n 次方. 对于该问题, n 是唯一的变量. 柯里化的作用, 就是避免在解决这样类似问题时, 重复调用无关的数字(如 2).

对于两个参数的情况, 我们可以写一个更通用的自动柯里化的函数, 以及对应的反柯里化函数:

```python
def curry2(f):
    '''Return a curried version of the given two-argument functions.'''
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    '''Return a two-argument version of the given curried function.'''
    def f(x, y):
        return g(x)(y)
    return f
```

## Lambda 表达式

截止到目前, 我们列举的函数, 都是有名字的. 但很多情况下, 我们并不需要对这个函数进行命名(有可能是一次性使用, 或者临时的闭包). 那么就需要祭出我们的另一神器: Lambda 表达式了.

```python
def compose1(f, g):
    return lambda x: f(g(x))
```

我们可以用对应的英语语法来理解 lambda 的语法:

| lambda           | x       | :           | f(g(x))  |
| ---------------- | ------- | ----------- | -------- |
| "A function that | takes x | and returns | f(g(x))" |

lambda 表达式的结果就是 lambda 函数. 除了没有名字以外, 它和其他正常的函数没有什么区别.

```python
f = compose1(lambda x: x*x, lambda y: y+1)
result = f(12) #169
```

虽然, 在 Python 里, lambda 表达式可以写的异常简洁, 如:

```python
compose1 = lambda f, g : lambda x : f(g(x))
```

但这样却某种程度上破坏了可读性, 让人乍一看, 比较糊涂.

所以通常情况下,  Python 还是会显式地使用 `def` 来表达函数. 但 lambda 函数仍会在返回值, 或是参数中经常出现.

## 抽象与一等公民

有经验的程序员往往会依照实际任务情况, 来选择抽象的级别. 基于一定的抽象基础, 做起事来将会得心应手. 就像上述长篇累牍地介绍的高阶函数, 我们完全可以将其看作一般的计算元素来处理.

通常, 在程序设计语言中, 对于可操控的计算元素, 都会加以限制. 这限制越少, 其地位则越高. 限制最少的计算元素, 我们成为语言的一等公民. 它的权利如下:

1. 他们可被命名
2. 他们可作为参数传递给函数
3. 他们可作为函数的返回值
4. 他们可被数据结构所包含

Python 授予了函数第一公民的奖章, 以至于其抽象表现能力, 被极大程度的加强了.

## 装饰模式

Python 提供了一种特殊的语法, 以便让高阶函数作为 `def` 语句的一部分, 参与执行过程. 这个被称之为**装饰者**.

```python
def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x
```

这其实相当于:

```python
triple = trace(triple)
```