# 282 class 클래스 상속

# 자동차 클래스 정의
class Car:
    # 생성자 정의
    # 바퀴, 가격 속성 정의 
    def __init__(self, wheel, price):
            self.wheel = wheel
            self.price = price

# Car 클래스 상속
# 자전거 클래스 정의
class Bicycle(Car):
      # 동작시 출력 문장
      print("나는야, 자전거!")

# 출력 문장 확인
print(Bicycle)

# 결과 :
# 나는야, 자전거!
# <class '__main__.Bicycle'>
