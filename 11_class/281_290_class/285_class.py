# 285 class 부모 클래스 생성자 호출
# *답안 확인

# 자동차 클래스 정의
class Car:
    # 생성자 정의
    # 바퀴, 가격 
    def __init__(self, wheel, price):
            self.wheel = wheel
            self.price = price

    # 부모 클래스
    # 생성자 호출 
    def Info(self):
        print("바큇 수 : ", self.wheel)
        print("가격 : ", self.price)
          

# 부모 클래스
# 생성자 정의
class Bicycle(Car):
    def __init__(self, wheel, price):
         super().__init__(wheel, price)

# Car 클래스 상속
# 자전거 클래스 정의
class Bicycle(Car):
      # 생성자 정의
      # 속성 정의
      # 바퀴, 가격
      # 생성자 추가 
      # 부품
      def __init__(self, wheel, price, part):
            # 부모 클래스
            # 생성자 정의
            super().__init__(wheel, price)
            self.part = part 

# 인스턴스 정의
bicycle = Bicycle(2, 100, "시마노")
# 바퀴, 가격 속성값 출력
print(bicycle.Info())

# 결과 :
# 바큇 수 :  2
# 가격 :  100
# None