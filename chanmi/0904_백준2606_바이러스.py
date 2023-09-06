def dfs(vertex):
    global count
    visited[vertex] = True
    count += 1

    for node in graph[vertex]:
        if not visited[node]:
            dfs(node)

# 노드 개수
PC_num = int(input())

# 간선 개수
net_num = int(input())

# 감염되는 컴퓨터 수
count = -1
visited = [False] * (PC_num + 1)

# 간선 설정
graph = [ [] for i in range(PC_num + 1)]

for i in range(net_num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
print(count)