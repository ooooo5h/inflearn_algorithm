n = int(input())
money_list = []

for _ in range(n) :
    
    nlist = list(map(int, input().split()))
    nlist.sort()
    
    if nlist[0] == nlist[1] == nlist[2] :
        money_list.append(10000 + (nlist[0] * 1000))
    elif nlist[0] == nlist[1] or nlist[1] == nlist[2] :
        money_list.append(1000 + (nlist[1] * 100))
    else :
        money_list.append(nlist[2] * 100)
    
    # print(money_list)
        
print(max(money_list))