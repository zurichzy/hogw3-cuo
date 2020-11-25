
class Animal:

    def eat(self):
        print('...吃东西...')

    def drink(self):
        print('.....喝水...')

    def sleep(self):
        print('....睡觉....')

class Dog(Animal):
    def drink(self):
        print('...小狗会叫...')

class Xiaogou(Dog):
    def run(self):
        print('....小狗会跑...')

class Cat(Animal):
    def catch(self):
        print('..小猫会抓老鼠....')


xiaogou1 =Dog()
xiaogou1.eat()
xiaoogu2 = Xiaogou()
xiaoogu2.sleep()
tom = Cat()
tom.drink()
