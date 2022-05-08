# 봉우리

# 상하좌우를 검색할 떄는 아래처럼 리스트를 하나 생성하자
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split()))  for _ in range(n)]
a.insert(0, [0]*n)  # 맨 위에 0 삽입
a.append([0]*n)   # 맨 아래에 0 삽입

for x in a :
    x.insert(0, 0)   # 왼쪽 0 삽입
    x.append(0)      # 오른쪽 0 삽입

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            # 위 반복문 4번을 돌면서 저게 다 참일 때
            cnt += 1
            
print(cnt)
    