# 288 class 메서드 오버라이딩

# 부모 클래스 
# 닭 
class Chicken:
  def call(self):
    print("부모호출")

# 부모 클래스 상속
# 자식 클래스
# 병아리 
class Chick(Chicken):
  def call(self):
    # 오버라이딩
    # 문장
    print("자식호출")

# 자식 클래스
me = Chick()
# 오버로딩 
me.call
# 오버로딩 문장 출력
print(me.call())

# 결과 :
# 자식호출