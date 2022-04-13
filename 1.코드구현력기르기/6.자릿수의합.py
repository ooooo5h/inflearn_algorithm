n = int(input())
nlist = list(map(int, input().split()))

def digit_sum(x) :
    sum = 0 
    for i in str(x):   # 파이썬스럽게 => str로 int처리하면 한 자리씩 사용 가능.
        sum += int(i)
        
    return sum

# print(digit_sum(7))  
# print(digit_sum(127))
# print(digit_sum(2254))

sum_list = []

for i in nlist :
    sum_list.append(digit_sum(i))
    
print(nlist[sum_list.index(max(sum_list))])