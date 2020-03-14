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

# 要把fib函数变成generator，只需要把print(b)改为yield b
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
# while True:  # 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration
#     # 的value中：
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

#九九乘法表
def table9_9(max=9):
    n=1
    while(n<=9):
        N=['{}*{}={}'.format(i,n,i*n) for i in range(1,n+1)]
        n=n+1
        yield N
T=table9_9()
for t in T:
    print(t)
# # test 杨辉三角
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)  # 想一想还是觉得很巧妙呀，在最后一个加上0，不管是第一个数或是最后一个数都是1+0
#         L = [L[i - 1] + L[i] for i in range(len(L))]



