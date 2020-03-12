# 迭代字典
# dict1 = {'a': 1, 'b': 2, 'c': 'test'}
# for i in dict1:
#     print(i)  #default : key

# for j in dict1.values():
#     print(j)    #value

# for k,v in dict1.items():
#     print(k,v)   #key value

# 判断迭代对象
# from collections.abc import Iterable
#
# print(isinstance('abc', Iterable))  # True
# print(isinstance(2.45, Iterable))  # False
# print(isinstance(123, Iterable))  # False

# 下标循环 enumberate()
# list1 = ['a', 'test', 'lala']
# for index, value in enumerate(list1):
#     print(index, value)

# 引用2个变量
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)

# 使用迭代查找一个list中最小和最大值，并返回一个tuple：
from collections.abc import Iterable


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif isinstance(L, Iterable) is True:
        max = L[0]
        min = L[0]
        for i in L:
            if min > i:
                min = i
            elif max < i:
                max = i
        return (min, max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
