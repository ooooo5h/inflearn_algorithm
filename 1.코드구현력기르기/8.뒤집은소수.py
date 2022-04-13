
def reverse(x) :
    return int(str(x)[::-1])

# print(type(reverse(1600)))

# 소수확인함수 => 소수면 리턴
def isPrime(x) :
    
    cnt = 0
    
    alist = [i for i in range(2, x+1)]
    
    for a in alist :
        if x % a == 0 :
            cnt += 1    
            
    if cnt == 1 :
        return x
        
        
# isPrime(13)
# isPrime(4)
# isPrime(7)

n = int(input())
nlist = list(map(int, input().split()))

for x in nlist :
    if isPrime(reverse(x)) :
        print(isPrime(reverse(x)), end=' ')
        