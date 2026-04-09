import sys
input = sys.stdin.readline

n = int(input())

ws = []

for _ in range(n):
    ws.append(input().strip())

ws = list(set(ws))

ws.sort(key = lambda x: (len(x), x))

for w in ws:
    print(w)