# 286 class 부모 클래스 생성자 호출

# 자동차 클래스
class Car:
    # 생성자 정의
    # 바퀴, 가격
    def __init__(self, wheel, price):
            self.wheel = wheel
            self.price = price

    # 부모 클래스
    # 생성자 호출
    # 바퀴, 가격
    def Info(self):
        print("바큇 수 : ", self.wheel)
        print("가격 : ", self.price)

# 차 클래스 
class Cars(Car):
     # 생성자 정의
     def __init__(self, wheel, price):
          super().__init__(wheel, price)
# 자전거 클래스
class Bicycle(Car):
    # 생성자 정의
    # 바퀴, 가격, 부품
    def __init__(self, wheel, price, part):
         super().__init__(wheel, price)
         self.part = part 

# 인스턴스 정의
bicycle = Bicycle(2, 100, "시마노")
# 부모 클래스 호출
bicycle.Info()

# 결과 :
# 바큇 수 :  2
# 가격 :  100