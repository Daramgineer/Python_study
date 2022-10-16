from random import *

class Unit:
    def __init__(self, name, hp): #__init__ : 객체 생성자. 
        self.name = name #맴버변수
        self.hp = hp
        print('{0} 유닛이 생성되었습니다.'.format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def move(self, location):
        print('{0} : {1} 방향으로 날아갑니다.'.format(self.name, location))

class Ground_Attack_Unit(Unit): #Unit class 상속
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp)
        self.damage = damage
        self.speed = speed

    def attack(self, location):
        print('{0} : {1} 방향으로 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

    def move(self, location): #함수 오버라이딩
        print('{0} : {1} 방향으로 움직입니다.'.format(self.name, location))

class Flyable_Attack_Unit(Ground_Attack_Unit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        Ground_Attack_Unit.__init__(self, name, hp, damage, 0) #지상속도 필요없음 0
        Flyable.__init__(self, flying_speed)

class Marine(Ground_Attack_Unit):
    def __init__(self):
        Ground_Attack_Unit.__init__(self, '마린', 40, 5, 1)

    def stimpack(self):
        if self.hp > 10:
            self.hp -=10
            print('{0} :  스팀팩을 사용합니다.'.format(self.name))
        else:
            print('{0} :  HP가 부족합니다.'.format(self.name))

class Tank(Ground_Attack_Unit):
    def __init__(self):
        Ground_Attack_Unit.__init__(self, '탱크', 50, 35, 1)
        self.seize_mode = False
    
    seize_developed = False #개발여부

    def set_sizemod(self):
        if Tank.seize_developed == False:
            return
        if Tank.seize_developed == True:
            if self.seize_mode == False:
                print('{0} : 시즈모드로 전환합니다.'.format(self.name))
                self.damage *= 2
                self.seize_mode = True
            else:
                print('{0} : 시즈모드를 해제합니다.'.format(self.name))
                self.damage /= 2
                self.seize_mode = False

class Wraith(Flyable_Attack_Unit):
    def __init__(self):
        Flyable_Attack_Unit.__init__(self, '레이스', 50, 15, 5)
        self.clocking_mode = False

    cloking_developed = False

    def set_clockingmod(self):
        if Wraith.cloking_developed == False:
            return
        if Wraith.cloking_developed == True:
            if self.clocking_mode == False:
                print('{0} : 스텔스모드로 전환합니다.'.format(self.name))
                self.cloking_mode = True
            else:
                print('{0} : 스텔스스모드를 해제합니다.'.format(self.name))
                self.cloking_mode = False

def game_start():
    print('새 게임을 시작합니다.')
def game_over():
    print('승리하였습니다.')


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

for unit in attack_unit:
    unit.move('1시')

Tank.seize_developed = True
print('[알림] : 시즈모드가 개발되었습니다.')
Wraith.cloking_developed = True
print('[알림] : 스텔스모드가 개발되었습니다.')

for unit in attack_unit:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_sizemod()
    elif isinstance(unit, Wraith):
        unit.set_clockingmod()

for unit in attack_unit:
    unit.attack('1시')

for unit in attack_unit:
    unit.damaged(randint(5, 50)) #데미지 5~20

game_over()

