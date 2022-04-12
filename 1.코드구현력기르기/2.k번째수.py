t = int(input())

for i in range(t):
    
    n,s,e,k = map(int, input().split())
    n_list = list(map(int, input().split()))
    
    n_list1 = n_list[s-1:e]
    n_list1.sort()
    print(n_list1)
    
    print(f'#{i+1} {n_list1[k-1]}')
