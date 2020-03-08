# def myabs(x):
#     if x>0:
#         return x
#     else:
#         return -x
# print(myabs(-3))
# 参数test
# 位置参数：
# def weizhi(name):
#     print(name + ' is your id!')
#
#
# weizhi('qiuyao')
# 默认参数
# def moren(name,age='18'):
#     print('your name is '+name,'your age is '+age)
#
#
# moren('qiuyao','20')
# moren('qiuyao')
# 可变参数
# def kebian(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
#     return sum
#
#
# kebian(1,3,5)

# 关键字参数
# def guanjianzi(name, **kw):
#     print('your name is ', name, 'youer city is ', kw)
#
#
# guanjianzi('qiuyao')
# guanjianzi('qiuyao',city='beijing',bogfriend='lixiaojie')
#命名关键字函数
# def mingming(name,*,age,sex):
#     print('name',name,'age',age,'sex',sex)
#
#
# mingming('qiuyao',age=18,sex='女')
# def person(name,*args,age,sex):
#     print('name',name,'qita',args,'age',age,'sex',sex)
#
#
# person('qiuyao',age=18,sex='女')
#test git