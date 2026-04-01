# 1. 입력 받기
n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결된 쌍의 수

# 2. 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 3. DFS로 감염시키기
visited = [False] * (n + 1)
count = 0

def dfs(now):
    global count
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            count += 1 # 새롭게 감염된 컴퓨터 카운트
            dfs(nxt)

# 1번 컴퓨터부터 시작
dfs(1)

# 4. 결과 출력
print(count)