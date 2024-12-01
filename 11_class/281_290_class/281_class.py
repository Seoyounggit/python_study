# 281~290

# 281 class 클래스 정의

# 자동차 클래스 정의
class Car:
    # 생성자 정의
    # 바퀴, 가격 속성 정의 
    def __init__(self, wheel, price):
            self.wheel = wheel
            self.price = price

# 객체 정의
car = Car(2, 1000)
# 바퀴, 자동차 속성값 출력
print(car.wheel)
print(car.price)
        
# 결과 : 
# 2
# 1000