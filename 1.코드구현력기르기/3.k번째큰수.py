n, k = map(int, input().split())

a = list(map(int, input().split()))

# sum = 0   sum이 따로 불필요
# res = [] 중복을 허용하지 않기 때문에 list를 사용하면 안된다.
res = set()   # set은 중복을 제거한다.

for i in range(n) :
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
            # print(i,j,m)
            
# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#           for k in range(j+1, n)
# 해도 되지만 위의 코드처럼 해도 
# i가 8이 되면 j가 9, m이 10이 되므로 m for문이 돌지않고 바로 멈추고 끝난다.

res = list(res)
res.sort(reverse=True)

print(res[k-1])