n = int(input())

for i in range(n) : 
    word = input().lower()
    
    if word == word[::-1] :
        result = 'YES'
    else :
        result = 'NO'
        
    print(f'#{i+1} {result}')
