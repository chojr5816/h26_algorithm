num_node = int(input())
num_edge = int(input())

graph = [[] for _ in range(num_node + 1)]
for _ in range(num_edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_list = []
def dfs(node):
    global count
    visited_list.append(node)
    count += 1
    for adj_node in graph[node]:
        if adj_node not in visited_list:
            dfs(adj_node)
count = 0
dfs(1)
print(count-1)