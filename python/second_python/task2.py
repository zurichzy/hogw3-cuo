'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造

'''
class Tonglao:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    def see_people(self,name):
        if name =='WZY' :
            print('师弟！！！')
        elif name == '李秋水':
            print('呸，贱人')
        elif name =='丁春秋':
            print('叛徒，我杀了你')

    def __new__(cls, *args, **kwargs):
        print('这是一场对战')
        return object.__new__(cls)



    def fight_zms(self,foe_hp,foe_power):
        self.hp /=2
        self.power *=10
        self.hp -=foe_hp
        foe_hp -=self.hp
        if self.hp >foe_hp:
            print('童姥你赢了')
        elif self.hp ==foe_hp:
            print('也就打了个平手')
        else:
            print('童姥，你没想到自己也有输的时候把')

class XuZhu(Tonglao):
    def read(self):
        print('罪过罪过')

xz = XuZhu(100,98)
xz.read()





