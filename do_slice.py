# 切片
# list1 = list(range(100))
# print(list1)
# print(list1[0:15])
# print(list1[-5:])
# print(list1[1:10:2])  # [1,3,5,7,9]
# print(list1[0:21:5]) #[0,5,10,15,20]
# def trim(s):
#     if s == '':
#         return s
#     else:
#         while s[0] == " ":
#             s = s[1:]
#         while s[-1] == ' ':
#             s = s[:-1]
#
#     return s

def trim(str):
    if str== '':
        return str
    elif (str[0]!=' ')and(str[-1]!=' '):
        return str
    elif str[0]==' ':
        return trim(str[1:])
    else:
        return trim(str[0:-1])



if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
