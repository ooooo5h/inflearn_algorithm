# 재귀함수를 이용한 이진수 출력
# 10진수 n이 입력하면 2진수로 변환하여 출력하는 프로그램을 작성해라

def change_to_binary(n):
    
    answer = []
    while n >= 1:    
        answer.append(n % 2)
        n = n // 2
    
    answer.reverse()
    
    for i in answer:
        print(i, end='')
    
change_to_binary(11)
