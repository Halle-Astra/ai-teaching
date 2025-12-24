#torch # lua --->C++ (暴露python，pytorch)

# 1. 变量 variable
# 2. 函数 function


# 1. 属性（属于类的变量，就叫属性/成员变量） property 
# 2. 方法（属于类的函数，就叫方法/成员函数） method
# atrribute = property+method的总称


from typing import Any

a = 10 # 全局变量
class student:
    abc = "alsj;f"
    def __init__(self, name, height, weight=98) -> None:
        # 只有__init__是实例化过程涉及到的。
        self.name = name # 属性
        self.height = height
        self.weight = weight
        self.a = 100 # 只属于实例化后的对象

    def run(self): # 方法
        print(a) # 10
        print(self.a) # 100
        print(self.name)
        self.a = 1000 

    def a(cls): # 约定俗成： 不需要实例化就自带的变量，用cls
        print(cls.abc)

    def __call__(self, ad):
        print('你输入了', ad)






jd  = student('asldf',149) # instantialize == >instance/object
# self是实例化以后的结果
# cls可以让人以为是类型本身，而非实例化才有的东西。
# student叫做类
# jd 叫做对象
# 类名() 是实例化
# 对象名() 是调用__call__ 

print(jd.name, 'weight:',jd.weight)
print('='*40)
jd.a()
print('*'*40)
print(student.abc)


jd(2334899)
