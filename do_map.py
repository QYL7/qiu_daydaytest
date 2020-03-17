# map map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。
# 有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
# def f(x):
#     return x*x
#
#
# r=map(f,[2,4,6,8])  # 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
# print(list(r))

# 把list所有数字转为字符串：
# print(list(map(str,[1,3,5,7,9])))  #['1', '3', '5', '7', '9']

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# 把序列[1, 3, 5, 7, 9]变换成整数13579
# from functools import reduce
#
#
# def fn(x,y):
#     return x*10+y
#
# print(reduce(fn,[1,3,5,7]))  #1357

# 练习1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
#     输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     return name.capitalize()
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)  #['Adam', 'Lisa', 'Bart']

# 练习2：请编写一个prod()函数，可以接受一个list并利用reduce()求积
# from functools import reduce
#
#
# def prod(L):
#     def multi(x, y):
#         return x*y
#     return reduce(multi, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

#练习3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# from functools import reduce
#
#
# def str2float(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     # 得到字符串中.的索引
#     n = s.index('.')
#     # 根据.的位置将字符串切片为两段
#     s1 = list(map(int, [x for x in s[: n]]))
#     s2 = list(map(int, [x for x in s[n + 1 :]]))
#     # m ** n表示m的n次方
#     return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')
