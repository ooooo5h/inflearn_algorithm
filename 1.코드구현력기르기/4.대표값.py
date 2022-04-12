import math

n = int(input())
n_list = list(map(int, input().split()))

average = math.ceil(sum(n_list) / n)  # 평균점수

# print(average)

# diff_list = []    리스트에 더하지말고, enumerate함수를 사용해서 구해보자!?
  
# for i in n_list :
#     diff_list.append(abs(average - i))
    
# print(diff_list)

min = 2147000000

for idx, val in enumerate(n_list) :
    
    tmp = abs(average - val)   # 차이
    
    if tmp < min :             
        min = tmp
        score = val
        res = idx + 1
        
    elif tmp == min :
        if val > score :
            score = val
            res = idx + 1
            
print(average, res)

