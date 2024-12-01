# 290 class 부모 생성자 호출

# 부모 클래스 
# 닭 
class Chicken:
  def __init__(self):
        print("부모생성")

# 부모 클래스 상속
# 자식 클래스
# 병아리 
class Chick(Chicken):
  def __init__(self):
        # 동작 문장
        print("자식생성")

        # 부모 클래스 생성자 정의
        super().__init__()

# 부모 클래스 호출
# 객체 정의
mom = Chicken()
# 동작 문장 출력
print(mom)

# 결과 :
# 부모생성