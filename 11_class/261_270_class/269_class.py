# 269 class 객체의 속성 수정 

# Stock 클래스 정의 
class Stock:
    # 생성자 정의
    # 종목명, 종목코드, PER, PBR, 배당수익률 생성자
    def __init__(self, name, code, per, pbr,dividend ):
        self.name = name
        self.code = code 
        self.per = per
        self.pbr = pbr 
        self.dividend = dividend
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, per):
        self.per = per

    # PBR 메서드 
    def set_pbr(self, pbr):
        self.pbr = pbr     

    def set_dividend(self, dividend):
        self.dividend = dividend


    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

# 기존 객체 
samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# PER 객체 속성 수정
samsung.set_per(12.75)
# 속성 호출
print(samsung.per)