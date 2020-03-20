# 在一个list中，删掉偶数，只保留奇数，可以这么写：

# def is_odd(n):
#     return n % 2 == 1
#
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# # 结果: [1, 5, 9, 15]

# 练习：回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    N=[]
    while n!=0:
        N.append(n%10)
        n = n // 10
    return N == N[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')