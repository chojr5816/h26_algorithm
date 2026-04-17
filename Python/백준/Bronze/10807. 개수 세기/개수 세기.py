import sys
input = sys.stdin.readline

n = int(input())
count = 0
num_list = list(map(int, input().split()))

v = int(input())
for i in num_list:
    if i == v:
        count += 1
print(count)