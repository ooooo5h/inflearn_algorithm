def change_to_number(word) : 
    number = ''
    for w in word :
        if not w.isalpha() :
            number += w
    
    return int(number)

def find_yaksu(x) :
    
    yaksu_list = []
    
    for i in range(1, x+1) :
        if x % i == 0 :
            yaksu_list.append(i)
    
    return len(yaksu_list)


word = input() 
print(change_to_number(word))
print(find_yaksu(change_to_number(word))) 
        
