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

![](http://composingprograms.com/img/pi_sum.png)

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

