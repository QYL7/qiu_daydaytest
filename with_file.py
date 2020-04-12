#1.文件读写

# f=open('/Users/lixiaojie/qiu/project1/test1.txt','r')  #打开文件
# print(f.read()) #读文件
# f.close() #关闭文件

#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
# try:
#     f = open('/Users/lixiaojie/qiu/project1/test1.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

#简洁写法：
# with open('/Users/lixiaojie/qiu/project1/test1.txt', 'r') as f:   #和前面的try ... finally是一样的
#     #print(f.read())  #查看全部
#     #print(f.readlines()) #按全部行查看
#     for line in f.readlines():
#         print(line.strip())  # 把末尾的'\n'删掉 ，行的格式查看

#2.二进制文件：
#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

# f = open('/Users/michael/test.jpg', 'rb')
# f.read()
#b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

# 3.字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# f.read()

#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，
# 表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

#f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

#4.写文件：
#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')
#注：以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
