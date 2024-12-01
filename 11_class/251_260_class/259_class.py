# 259 class 클래스 소멸

# Human 클래스 정의 
class Human:
    # self로 메서드 정의 
    # 이름, 나이, 성별이라는 속성
    def __init__(self, name, age, gander):
        # 생성자 정의 
        self.name = name
        self.age = age
        self.gender = gander 
    
    # 클래스 소멸
    def __del__(self):
        print("나의 죽음을 알리지마라")

    # 메서드1 정의    
    def who(self):
        print("이름 : {} 나이{} 성별 {}".format(self.name, self.age, self.gender))

    # 메서드2 정의
    # 이름, 나이, 성별이라는 속성
    def setInfo(self, name, age, gander):
        self.name = name
        self.age = age
        self.gender = gander 

# 객체 생성자
# 속성값 정의 
areum = Human("아름", 25, "여자")
# 소멸
del(areum)

# 결과 : 나의 죽음을 알리지마라