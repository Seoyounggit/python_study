# 289 class 생성자

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

# 자식 클래스 호출
# 객체 생성
me = Chick()
# 동작 문장 호출
print(me)

# 결과 :
# 자식생성