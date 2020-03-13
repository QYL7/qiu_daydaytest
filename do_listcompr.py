# 列表生成式

# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# L = list(range(1, 11))
# print(L)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# L=[ ]
# for i in list(range(1,11)):
#     L.append(i*i)
# print(L)

# L = [i * i for i in list(range(1, 11))]
# print(L)

# L = [i * i for i in list(range(1, 11)) if i % 2 == 0]
# print(L)    #仅偶数的平方

# 使用两层循环，可以生成全排列：

# L = [m + n for m in 'ABC' for n in 'XYZ']
# print(L)   #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# import os
#
# f = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
# print(f)  # ['.git', '.idea', 'def_dict.py', 'do_iter.py', 'do_listcompr.py', 'do_slice.py', 'README.md', 'readme.txt', 'recur.py', 'test.py', 'test1.txt', 'venv']

# 列表生成式也可以使用两个变量来生成list：
# dict1 = {'a': '1', 'test': '23', 'c': '9'}
# dict2 = [k + '=' + v for k, v in dict1.items()]
# print(dict2)

#把一个list中所有的字符串变成小写
# L=['MIKE','LILY','JACK']
# L1=[i.lower() for i in L]
# print(L1)

#列表表达式中的if--else
#在for后面的if是一个筛选条件，不能带else
# L=[i*i for i in range(1,11) if i%2==0]
# print(L)
#把if写在for前面必须加else
# L=[x*x if x%2==0 else -x for x in range(1,11)]
# print(L) # [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100]

#练习

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [i.lower() for i in L1 if isinstance(i,str)]
#
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')
