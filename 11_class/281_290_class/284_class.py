# 284 class 클래스 상속 생성자 추가

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
      # 생성자 추가 
      # 부품
      def __init__(self, wheel, price, part):
            self.wheel = wheel
            self.price = price
            self.part = part 

# 인스턴스 정의
bicycle = Bicycle(2, 100, "시마노")
# 바퀴, 가격 속성값 출력
print(bicycle.wheel)
print(bicycle.price)
# 속성값 추가
# 부품 속성값 출력
print(bicycle.part)

# 결과 :
# 2
# 100
# 시마노