n, m = map(int, input().split())

cnt = [0] * (n+m+2)
# print(cnt)

for i in range(1, n+1) :
    for j in range(1, m+1) :
        sum = i + j
        cnt[sum] += 1
        
# print(cnt)   
# print(max(cnt))
# print(cnt.index(max(cnt)))
# 맥스값이 여러개인데.. 그걸 한번에 어떻게 출력하나 => 내 생각 : 반복문으로?

for idx, val in enumerate(cnt) :
    if val == max(cnt) :
        print(idx, end = ' ')