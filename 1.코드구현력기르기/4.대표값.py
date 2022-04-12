import math

n = int(input())
a = list(map(int, input().split()))

avg_a = math.ceil(sum(a)/n)  # 평균

min = 214700000 # 가장 큰 수를 가정해 대입해놓고, min값 덮어쓰기

# 학생의 번호를 출력해야한다 => 학생의 idx가 필요 => enumerate
for idx, val in enumerate(a):
    
    minus = abs(avg_a - val)
    
    if minus < min :
        min = minus
        score = val    # 차가 같으면, 더 큰 점수가 정답이니까 점수를 저장해야한다
        res = idx + 1  # 점수차가 동일하면, 빠른 학생번호가 정답이라 저장해야하고, 1부터 시작한다했으니 +1을 해야한다.
    
    elif minus == min :  # 차이가 같은 경우!
        # 점수를 비교하기
        if score < val :  # 현재 val이 더 크면 val이 정답
            score = val
            res = idx + 1
            # 아예 똑같은 점수를 발견하면 이 if문 내부로는 들어가지않음
            # 맨 앞의 idx가 담겨있다.
            
print(avg_a, res)
    