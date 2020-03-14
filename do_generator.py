# 创建生成器
# L = [i * i for i in range(1, 11)]
# g = (i * i for i in range(1, 11))


# print(g)  # <generator object <genexpr> at 0x103311450>
# print(next(g))  # 1
# print(next(g))  # 4
# print(next(g))  # 9
# print(next(g))  # 16

# for j in g:
#     print(j)   #通过for循环来迭代

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# def fib(x):
#     n, a, b = 0, 0, 1
#     while n < x:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return "done"
#
#
# fib(10)

# 1.要把fib函数变成generator，只需要把print(b)改为yield b
# def fib(x):
#     n, a, b = 0, 0, 1
#     while n < x:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return "done"
#
#
# f = fib(10)
# for i in f:
#     print(i)


# 2.按照列表打印
# def fib(x):
#     i, a, b = 0, 0, 1
#     fib_list = []
#     while (i < x):
#         fib_list.append(b)
#         yield fib_list
#         a, b = b, a + b
#         i = i + 1
#
#
# f = fib(10)
# for n in f:
#     print(n)

# while True:  # 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration
#     # 的value中：
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# 九九乘法表
# def table9_9(max=9):
#     n = 1
#     while (n <= 9):
#         N = ['{}*{}={}'.format(i, n, i * n) for i in range(1, n + 1)]
#         n = n + 1
#         yield N
#
#
# T = table9_9()
# for t in T:
#     print(t)


# # test 杨辉三角：
# 方法1：
# def triangle(max):
#     N = [1]
#     n = 0
#     while n < max:
#         yield N
#         N.append(0)  #N[0]=1
#         N = [N[i - 1] + N[i] for i in range(len(N))]
#         n += 1
#
#
# for t in triangle(10):
#     print(t)

# 方法2：
# def triangles():
#     p = [1]
#     while True:
#         yield p  # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
#         p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]
#
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break
