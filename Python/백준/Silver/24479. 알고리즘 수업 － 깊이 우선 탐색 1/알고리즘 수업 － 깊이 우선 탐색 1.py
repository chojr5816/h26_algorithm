import sys

# 재귀 한도 설정
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# 입력 받기
N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)  # 저장값
count = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # 양 방향 간선
    graph[b].append(a)  # 양 방향 간선

def dfs(t):
    global count
    visited[t] = count
    graph[t].sort()
    for i in graph[t]:
        if visited[i] == 0:
            count += 1
            dfs(i)

dfs(R)
for i in range(1, N+1):
    print(visited[i])