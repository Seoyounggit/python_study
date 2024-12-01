# 255 class 클래스 생성자 2

# Human 클래스 정의
class Human:
    # self로 생성자 정의
    # 이름, 나이, 성별
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 
        
# areum 인스턴스 생성
# 객체의 속성 정의  
areum = Human("아름", 25, "여자")
print(areum.name, areum.age, areum.gender)

# 결과 : 아름 25 여자
