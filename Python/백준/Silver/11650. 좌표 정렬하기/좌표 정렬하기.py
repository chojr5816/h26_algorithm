import sys
input = sys.stdin.readline

n = int(input())

loc = []

for _ in range(n):
    loc.append(list(map(int, input().split())))

loc.sort()

for i in range(n):
    print(loc[i][0], loc[i][1])