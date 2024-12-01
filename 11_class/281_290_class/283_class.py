# 293 class 클래스 상속 생성자 정의

# 자동차 클래스 정의
class Car:
    # 생성자 정의
    # 바퀴, 가격 
    def __init__(self, wheel, price):
            self.wheel = wheel
            self.price = price

# Car 클래스 상속
# 자전거 클래스 정의
class Bicycle(Car):
      # 생성자 정의
      # 속성 정의
      # 바퀴, 가격 
      def __init__(self, wheel, price):
            self.wheel = wheel
            self.price = price

# 객체 정의
bicycle = Bicycle(2,100)
# 바퀴, 가격 속성값 출력
print(bicycle.wheel)
print(bicycle.price)

# 결과 :
# 2
# 100