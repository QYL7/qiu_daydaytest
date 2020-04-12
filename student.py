class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def set_score(self,score):
        if 0<=score<=100:   #参数校验
            self.__score=score
        else:
            print("输入无效！")

    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))

std1=Student('lily',89)
std1.set_score(88)
print(std1.get_score())



