# 258 class 클래스 메서드 2

# Human 클래스 정의 
class Human:
    # self로 메서드 정의 
    # 이름, 나이, 성별이라는 속성
    def __init__(self, name, age, gander):
        # 생성자 정의 
        self.name = name
        self.age = age
        self.gender = gander 

    # 메서드1 정의    
    def who(self):
        print("이름 : {} 나이{} 성별 {}".format(self.name, self.age, self.gender))

    # 메서드2 정의
    # 이름, 나이, 성별이라는 속성
    def setInfo(self, name, age, gander):
        self.name = name
        self.age = age
        self.gender = gander 

# 객체 생성1
# 속성값 정의
areum = Human("모름", 0, "모름")
# 메서드 호출1
areum.who()

# 객체 생성2
# 속성값 정의
areum.setInfo("아름", 25, "여자")
# 메서드 호출2
areum.who()

# 결과 :
# 이름 : 모름 나이0 성별 모름
# 이름 : 아름 나이25 성별 여자