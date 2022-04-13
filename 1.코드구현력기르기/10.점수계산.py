n = int(input())
alist = list(map(int, input().split()))

cnt = 0
sum = 0

for a in alist :
    if a == 0 :
        cnt = 0
        
    else :
        cnt += 1
        sum += cnt
        
print(sum)