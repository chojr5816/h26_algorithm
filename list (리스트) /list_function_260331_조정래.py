#정수로 구성되어 있는 리스트를 파라미러토 입력받아 다음의 기능을 수행하는 함수 구현
number_list = [23, 45, 27, 11, 25, 65, 78]

def getIndex(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target:
            return i
    return -1

def getMax(num_list):
    if not num_list: 
        return None
    
    max_num = num_list[0]
    
    for n in num_list:
        if n > max_num:
            max_num = n
    return max_num

def getMin(num_list):
    if not num_list: 
        return None
    
    min_num = num_list[0]
    
    for n in num_list:
        if n < min_num:
            min_num = n
    return min_num

def countGT(num_list, target):
    count = 0
    for n in num_list:
        if n > target:
            count += 1
    return count

def sumList(num_list):
    total = 0
    for n in num_list:
        total += n
    return total

def swapList(num_list):
    left = 0
    right = len(num_list) - 1
    
    while left < right :
        num_list[left], num_list[right] = num_list[right], num_list[left]
        
        left += 1
        right -= 1


print(getIndex(number_list, 25))  
print(getMax(number_list))          
print(getMin(number_list))          
print(countGT(number_list, 42))    
print(sumList(number_list))         
print(swapList(number_list))
print(number_list)
