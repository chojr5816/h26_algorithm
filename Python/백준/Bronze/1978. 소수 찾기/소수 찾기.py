def is_prime_number(num):
    if num == 1:
        return False
    for i in range(2, num//2+1):
        if num%i==0:
            return False
    return True


N = int(input())

count = 0
num_list = map(int, input().split())

for num in num_list:
    if is_prime_number(num):
        count += 1
print(count)