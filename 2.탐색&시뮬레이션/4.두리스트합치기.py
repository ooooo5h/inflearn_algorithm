# n = int(input('리스트의 크기 : '))
# nlist = list(map(int, input('리스트 원소들 입력 : ').split()))
# m = int(input('두번째 리스트의 크기 : '))
# mlist = list(map(int, input('두번째 리스트 원소들 입력 : ').split()))

# print(sorted(nlist + mlist))

# 이렇게 풀었는데.. 정렬되있다는 사실을 사용하라는 의미. 
# 이렇게 풀라는 게 아니였다.

n = int(input('리스트의 크기 : '))
a = list(map(int, input('리스트 원소들 입력 : ').split()))
m = int(input('두번째 리스트의 크기 : '))
b = list(map(int, input('두번째 리스트 원소들 입력 : ').split()))

c = []
p1 = p2 = 0

while True :
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else :
        c.append(b[p2])
        p2 += 1
        
    if p1 < n :
        # n리스트를 다 순환 돌았다, m리스트는 남아있다.
        c = c + a[p1:]
        break
            
    elif p2 < m :
        c = c + b[p2:]
        break 
    
for a in c :
    print(a, end = ' ')