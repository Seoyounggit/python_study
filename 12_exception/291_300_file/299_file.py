# 299 file 예외 처리 메세지 

# data 리스트
data = [1, 2, 3]

# 입력 값
for i in range(5):
    # 실행 코드
    try:   
        print(data[i])

    # 예외 처리
    # 별칭 err
    except IndexError as err:
        # 예외 처리 메세지 출력
        print(err)
        print('에러 발생! 예외 처리 시도')
# 결과 :
# 1
# 2
# 3
# list index out of range
# 에러 발생! 예외 처리 시도
# list index out of range
# 에러 발생! 예외 처리 시도