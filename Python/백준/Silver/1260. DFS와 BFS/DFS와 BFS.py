from collections import deque
N, M, start = map(int, input().split())

# 그래프 만들기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_list = []
queue = deque()

def dfs(node):
    visited_list.append(node)
    print(node, end= ' ')
    for adj_node in sorted(graph[node]):
        if adj_node not in visited_list:
            dfs(adj_node)

def bfs(start):
    queue.append(start)
    while queue:
        node = queue.popleft()
        visited_list.append(node)
        print(node, end = ' ')
        for adj_node in sorted(graph[node]):
            if adj_node not in visited_list:
                if adj_node not in queue:
                    queue.append(adj_node)

dfs(start)
print()
visited_list.clear()
bfs(start)