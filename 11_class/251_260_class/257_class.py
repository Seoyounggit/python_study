# 257 class 클래스 메서드 1 *답안 확인

# Humam 클래스 정의 *답안 확인
class Human:
    # self 로 생성자 정의 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 메서드 정의
    def who(self):
        # 메서드 출력 
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.gender))

# 인스턴스 생성
areum = Human("조아름", 25, "여자") 

# 메서드 호출
areum.who()
        
# 결과 : 
# 이름: 조아름 나이: 25 성별: 여자        