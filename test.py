# # lixiaojie={'nose':1,'eyes':2,'face':['big','white']}
# # print(lixiaojie['face'][0])
# s={'a':'1','c':'2','b':'3'}
# print(sorted(s))
# file = open('test1.txt','w')
# file.write('hello world!')
# file.close()
# f=open('test1.txt')
# t=f.read()
# print(t)
# class work:
#     def __init__(self, name, pay):
#         self.name = name
#         self.pay = pay
#
#         def lastName(self):
#             return self.name.split()[-1]
#
#         def giveRaise(self,percent):
#             return self.pay(1.0+percent)

# age = input("age:")
# age=int(age)
# if age < 6:
#     print("you are kid")
# elif age > 20:
#     print("you are adult")
# else:
#     print("you are teenager")

# name = ["mike", "lila", 'lulu']
# for x in name:
#     print(x)
# L = ['Bart', 'Lisa', 'Adam']
# for i in L:
#     print("hello!"+i)

# while 1:
#     print('END')
# dict1 = {"mike": 95, "jack": 98}
# #print(dict1["mike"])
# # dict1["jack"]= 88
# # print("lp" in dict1)
# # print(dict1.get("mama"))
# dict1.pop(0)
# print(dict1)
# s1=set([1,2,3,3,4])
# s2=set(['a','b','c'])
# print(s1&s2)
# print(s1|s2)

#求一个列表里和等于10的个数
# list=[2,8,1,3,4,9,6,7]
# count=0
# for i in range(len(list)-1):
#    # print(i)
#     for j in range(i+1,len(list)):
#       #  print(j)
#         if list[i]+list[j]==10:
#             print(i,j)
#             count=count+1
# print(count)

#字符串求差集 a-b
# a='abdghh34'
# b='12dfghh'
# for i in a:
#     for j in b:
#         if i==j:
#             a=a.replace(i,'')
# print(a)


