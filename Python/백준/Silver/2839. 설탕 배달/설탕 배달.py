N = int (input())

# 자료 구조 정의
# 5kg, 3kg의 최대 봉지수
max_5kg = N // 5
max_3kg = N // 3
min_bag = max_5kg + max_3kg
is_found = False

# 알고리즘
for num_5kg in range(max_5kg + 1):
    for num_3kg in range(max_3kg + 1):
        if num_5kg * 5 + num_3kg * 3 == N:
            is_found = True
            cur_bag = num_5kg + num_3kg
            if min_bag > cur_bag:
                min_bag = cur_bag
if is_found: # N kg이 되는 봉지 수가 없으면 
    print (min_bag)
else:
    print(-1)