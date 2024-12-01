# 261 class 생성자

# Stock 클래스 정의
class Stock:
    # 메서드 정의
    # 종목명과 종목코드 속성 생성
    def __init__(self, name, code):
        self.name = name
        self.code = code

# 인스턴스 정의
# 속성 정의
samsung = Stock("삼성전자", "005930")
# 메서드 호출
print(samsung.name)
print(samsung.code)

# 결과 :
# 삼성전자
# 005930