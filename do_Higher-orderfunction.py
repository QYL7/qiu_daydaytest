# 高阶函数：既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 绝对值的函数abs()

f = abs
def add(x, y, f):
    return f(x) + f(y)  # f(x) + f(y) ==> abs(1) + abs(-8) ==> 9


z = add(1, -8, abs)
print(z)

