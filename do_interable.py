# 使用isinstance()判断一个对象是否是Iterable对象
from collections.abc import Iterator
# from collections.abc import Iterable
#
# print(isinstance([],Iterable))
# print(isinstance('abc',Iterable))
# print(isinstance(123,Iterable))

#使用isinstance()判断一个对象是否是Iterator对象：
# print(isinstance([],Iterator))
# print(isinstance((x for x in []),Iterator))

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]),Iterator))


