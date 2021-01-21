#연습문제
#Knight 클래스를 만들고 제시된 값들을 넘겨주면서 객체 생성
# slash()메소드 만들기
'''
class Knight:
    def __init__ (self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기 시전')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()
'''
class Annie:
    #생성자 메소드 생성, (파라미터로 health, mana, ability_power를 받음)
    def __init__ (self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    
    def tibbers(self):
        AP = self.ability_power * 0.65 + 400
        print('티버: 피해량', AP)


health, mana, ability_power = map(float, input().split())

#인스턴스 생성, input으로 입력받은 변수들을 argument로 넘김
x = Annie(health=health, mana=mana, ability_power=ability_power)
# x객체의 메소드 trbbers() 접근
x.tibbers()

