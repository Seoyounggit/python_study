# 274 class  입금 메서드

# 랜덤 모듈
import random

# 은행 클래스
class Account:
    # 계좌 객체의 개수 
    cnt = 0

    # 이름, 계좌 번호
    def __init__(self, name, num):
        self.name = name
        self.num = num
        # 은행명 
        self.bank = "SC은행" 
        
        # 계좌 번호
        # 랜덤 생성
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        # 계좌 번호  
        # 3자리-2자리-6자리
        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)      

        # 통장잔액
        self.account_number = num1 + '-' + num2 + '-' + num3  

        # 계좌 객체의 갯수
        Account.cnt += 1

    # 클래스 메서드  
    @classmethod
    def get_account_num(clsm):
            print(clsm.cnt)

    # 입금 메서드
    def deposit(self, deposit):
        if deposit >= 1:
            self.num += deposit


# 셍성자 정의1,2
# 계좌 객체1, 2
# 입금 
hwang = Account("황서영", 100)
hwang.deposit(1000)
kim = Account("김감자", 200)
kim.deposit(2000)
