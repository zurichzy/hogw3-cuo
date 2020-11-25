
#面向对象
class House:
    #静态属性--变量，也是类变量，在类之中，方法之外
    door = 'red'
    floor = 'white'

    #动态属性--方法（函数）
    def __init__(self):
        #实例变量，类变量，方法之内，以self.变量名的方法定义
        #实例变量的作用域为这个类中的所有方法
        print(self.door)

    def sleep(self):
        #普通变量在类之中，方法之外，并且不会以self.
        print('用来睡觉')

    def cook(self):
        print('可以做饭')
#实例化 --变量=类（）
nor_house =House
china_honse = House

#调用类变量
print(House.door)

