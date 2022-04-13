n = int(input())

alist = [0] * (n+1)
cnt = 0

for i in range(2, n+1) :
    if alist[i] == 0 :
        cnt += 1
        # print('cnt', cnt)
        
        for j in range(i, n+1, i) :
            alist[j] = 1
            # print('alist', alist)

print('정답', cnt)