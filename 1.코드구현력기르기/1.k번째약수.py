n, k = map(int, input().split())

a_list = []

for i in range(1, n+1) :
    
    if n % i == 0 :
        a_list.append(i)

# print(a_list)  # 약수가 담겨있음

if len(a_list) < k :
    print(-1)
    
else :
    print(a_list[k-1])