# 275 class ��� �޼���

# ���� ���
import random

# ���� Ŭ����
class Account:
    # ���� ��ü�� ���� 
    cnt = 0

    # �̸�, ���� ��ȣ
    def __init__(self, name, num):
        self.name = name
        self.num = num
        # ����� 
        self.bank = "SC����" 
        
        # ���� ��ȣ
        # ���� ����
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        # ���� ��ȣ  
        # 3�ڸ�-2�ڸ�-6�ڸ�
        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)      

        # �����ܾ�
        self.account_number = num1 + '-' + num2 + '-' + num3  

        # ���� ��ü�� ����
        Account.cnt += 1

    # Ŭ���� �޼���  
    @classmethod
    def get_account_num(clsm):
            print(clsm.cnt)

    # �Ա� �޼���
    def deposit(self, deposit):
        if deposit >= 1:
            self.num += deposit
    
    # ��� �޼���
    def withdrawal(self, withdrawal):
        if self.deposit > withdrawal:
            self.deposit -= withdrawal


# �ļ��� ����1,2
# ���� ��ü1, 2
# �Ա� 
hwang = Account("Ȳ����", 100)
hwang.deposit(1000)
kim = Account("�谨��", 200)
kim.deposit(2000)