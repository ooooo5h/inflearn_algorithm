n, k = map(int, input().split())
a = list(map(int, input().split()))

sum_res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            sum_res.add(a[i]+a[j]+a[m])

sum_res = list(sum_res)
sum_res.sort(reverse=True)
print(sum_res[k-1])
