import sys
input = sys.stdin.readline

n = int(input())
stus = []

for _ in range(n):
    stus.append(input().split())

stus.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for stu in stus:
    print(stu[0])