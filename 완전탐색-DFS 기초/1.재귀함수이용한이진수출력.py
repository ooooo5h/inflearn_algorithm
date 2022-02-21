# 재귀함수를 이용한 이진수 출력
# 10진수 n이 입력하면 2진수로 변환하여 출력하는 프로그램을 작성해라

def change_to_binary(n):
    # 재귀함수 사용 시 종료조건 필수!!
    if n == 0:
        return
    
    else :
        # n을 2 로 나눈 나머지가 이진수에 해당하는 숫자
        print(n%2, end='')
        # n을 2로 나눈 몫은 또 나눠줘야하니까 재귀함수호출 시 파라미터로 전달
        change_to_binary(n//2)
    
change_to_binary(11)
