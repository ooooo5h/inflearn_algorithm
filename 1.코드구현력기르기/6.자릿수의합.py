n = int(input())
nlist = list(map(int, input().split()))

def digit_sum(x) :
    sum = 0 
    for _ in range(len(str(x))) :
        a = x % 10
        x = x // 10
        sum += a
        
    return sum

# print(digit_sum(7))
# print(digit_sum(127))
# print(digit_sum(2254))

sum_list = []

for i in nlist :
    sum_list.append(digit_sum(i))
    
print(nlist[sum_list.index(max(sum_list))])