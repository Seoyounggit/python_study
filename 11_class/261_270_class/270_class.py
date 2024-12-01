# 270 class 여러 종목의 객체 생성 
# * 답안 확인

# 클래스 정의
class Stock:
    # 생성자 정의
    # 종목명, 종목코드, PER, PBR, 배당수익률 생성자
    def __init__(self, name, code, per, pbr,dividend ):
        self.name = name
        self.code = code 
        self.per = per
        self.pbr = pbr 
        self.dividend = dividend
    
    # 메서드 정의 
    # 종목명 메서드
    def set_name(self, name):
        self.name = name

    # 종목코드 메서드
    def set_code(self, code):
        self.code = code

    # PER 메서드
    def set_per(self, per):
        self.per = per

    # PBR 메서드
    def set_pbr(self, pbr):
        self.pbr = pbr  

    # 배당수익률 메서드 
    def set_dividend(self, dividend):
        self.dividend = dividend

    # 메서드 속성 업데이트
    # 종목명 메서드 속성 업데이트
    def get_name(self):
        return self.name

    # 종목코드 메서드 속성 업데이트
    def get_code(self):
        return self.code

    # PER 메서드 속성 업데이트
    def get_per(self):
        return self.per

    # PBR 메서드 속성 업데이트
    def get_pbr(self):
        return self.pbr
    
    # 배당수익률 메서드 속성 업데이트
    def get_dividend(self):
        return self.dividend

# 종목 리스트 초기화 
event = []
# 객체 정의
# 속성 정의
# 삼성전자 
samsung = Stock('삼성전자','005930',15.79,1.33,2.83)
# 현대차 
hyundai = Stock('현대차','005380',8.70,0.35,4.27)
# LG전자 
lg = Stock('LG전자','066570',317.34,0.69,1.37)

event.append(samsung)
event.append(hyundai)
event.append(lg)

# 속성 출력
# 종목코드, PER 
for x in event:
    # X로 객체 바인딩
    print(x.code, x.per)

# 결과 :
# 005930 15.79
# 005380 8.7
# 066570 317.34


