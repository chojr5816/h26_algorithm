import sys

# 1. 재귀 한도 설정 (DFS 사용 시 필수)
sys.setrecursionlimit(10**6)

# 2. 빠른 입력 함수 설정
# input() 대신 sys.stdin.readline을 사용하면 읽기 속도가 수십 배 빠릅니다.
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# N: 정점 개수, M: 간선 개수
try:
    line = input().split()
    if not line:
        exit()
    n, m = map(int, line)

    # 인접 리스트 생성
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    count = 0

    # 연결 요소 탐색
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1

    print(count)

except EOFError:
    pass