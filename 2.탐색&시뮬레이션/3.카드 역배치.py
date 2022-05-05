cards = list(range(21))

# 10개의 구간이 주어지니까 10번만 돌면 됨
for _ in range(10): 
    a, b = map(int, input().split()) 
    
    for i in range((b-a+1)//2) : # 뒷숫자-앞숫자+1를 2로 나눈 몫만큼 순서를 바꾼다.
        # 앞숫자a는 뒤로 움직이고, 뒷숫자b는 앞으로 움직여야한다.
        cards[a+i], cards[b-i] = cards[b-i], cards[a+i]

# 여기서 cards는 다 바뀌어있지만, 앞에 0이 속해있다.
# 0을 삭제하고, 리스트가 아닌 숫자를 출력해야한다.
cards.pop(0)

for c in cards:
    print(c, end=' ')
    