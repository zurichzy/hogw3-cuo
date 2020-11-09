#回合制游戏
#一个多回合制游戏，每个角色都有hp 和power，
# hp代表血量，power代表攻击力，hp的初始值为1000，
# power的初始值为200。打斗多个回合
# 定义一个fight方法：
# my_hp = hp - enemy_power
# enemy_final_hp = enemy_hp - my_power
# 谁的hp先为0，那么谁就输了

def game():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 200
    my_final_hp =my_hp - your_power
    enemy_final_hp = your_hp - my_power
    #三目运算等同于if_else
    #print("我赢了") if my_final_hp > enemy_final_hp else print('你赢了')
    if my_final_hp > enemy_final_hp:
        print('我赢了')
    else:
        print('你赢了')

game()

