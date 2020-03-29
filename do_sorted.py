# Python内置的sorted()函数就可以对list进行排序：
# print(sorted([1,4,-1,8,-3])) #1
# list=[1,4,-1,8,-3]
# list2=sorted(list)
# print(list2)                 #2

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
#print(sorted([1,4,-1,8,-3],key=abs))  #[1, -1, -3, 4, 8]  key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序

#字符串排序
#1.正常：
#print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#结果： ['Credit', 'Zoo', 'about', 'bob']

#2.忽略大小写：传入第二个参数
#print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#结果： ['about', 'bob', 'Credit', 'Zoo']

#3.反向排序：可以传入第三个参数reverse=True：
#print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))
#结果： ['Zoo', 'Credit', 'bob', 'about']

#练习：
# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
# from operator import itemgetter
#
# students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# print(sorted(students, key=itemgetter(0)))  #按名字
# print(sorted(students, key=lambda t: t[1])) #按成绩
# print(sorted(students, key=itemgetter(1), reverse=True)) #按成绩降序
