class Human:
    def physical(self, height, weight, squat=0, benchpress=0, deadlift=0): 
        #초깃값을 설정 해 줄수 있다. 
        #특히 뒤 3개같이 절대 존재하는 속성이 아닌것들에 대해서
        self.h = height
        self.w = weight
        self.s = squat
        self.b = benchpress
        self.d = deadlift
        
        strength = self.s + self.b + self.d
        return (self.h, self.w , strength)
        
class Father(Human):
    lastnamefather = '이' #클래스 변수 선언
    def FirstName(self, first):
        self.firstname = first
        return self.firstname

class Mother(Human):
    lastnamemother = '김'
    def FirstName(self, first):
        self.firstname = first
        return self.firstname

class Son(Father,Mother):
    def Lname(self):
        return self.lastnamefather
            
class Daughter(Father,Mother):
    def Lname(self):
        return self.lastnamemother

class VeryWeakSon(Father, Mother):
    def Lname(self):
        return self.lastnamefather

a = Father()
b = Mother()
c = Son()
d = Daughter()
e = VeryWeakSon()

print('아빠 스펙')
print('(키, 몸무게, 3대): ', a.physical(180, 80, 200, 140, 205))
print(a.lastnamefather, end = ' ')
print(a.FirstName('춘식'))
print()
print('엄마 스펙')
print('(키, 몸무게, 3대): ', a.physical(165, 58, 160, 100, 200))
print(b.lastnamemother, end = ' ')
print(b.FirstName('춘희'))
print()
print('아들 스펙')
print(c.Lname(), end = ' ')
print(c.FirstName('철수'))
print('(키, 몸무게, 3대) : ', c.physical(185, 100, 280, 200, 300))
print()
print('딸 스펙')
print('(키, 몸무게, 3대): ', a.physical(168, 63, 180, 120, 210))
print('딸의 이름은')
print(d.Lname(), end = ' ')
print(d.FirstName('영희'))
print()
print('매우 약한 아들 스펙')
print('(키, 몸무게, 3대: ', e.physical(183, 55))
print(e.lastnamefather, end = ' ')
print(e.FirstName('꽁치'))




