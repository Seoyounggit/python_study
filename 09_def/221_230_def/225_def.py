# 225 def

# 함수 정의
# 매개변수 정의
def print_value_by_key(my_dict, k):  
        # 매개변수에 입력된 value값을 key값으로 찾아 호출
        # value[key]
        print(my_dict[k])

# 파라미터 값
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

# 리스트 value를 key로 찾기
print_value_by_key(my_dict, "10/26")

# 결과 :
# [100, 130, 100, 100]