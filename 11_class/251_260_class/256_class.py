# 256 class 인스턴스 접근

# Human 클래스 정의
class Human:
    # self 로 생성자 정의
    # 이름, 나이, 성별 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 
        
# 인스턴스 생성자
areum = Human("조아름", 25, "여자")
# 나이, 이름, 성별 생성자 출력
# 인스턴스 속성 접근
print("이름: ", areum.name, ", 나이: ", areum.age, ", 성별: ", areum.gender)

# 결과 :
# 이름:  조아름 , 나이:  25 , 성별:  여자
