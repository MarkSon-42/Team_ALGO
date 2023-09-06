def dfs(vertex, distance):
    visited[vertex] = True
    distance += 1
    if vertex == t2:
        family_list.append(distance)

    for node in graph[vertex]:
        if not visited[node]:
            dfs(node, distance)

# 노드 개수
people_num = int(input())

# 목표 사람들
t1, t2 = map(int, input().split())

# 간선 개수
m = int(input())

family_list = []
visited = [False] * (people_num + 1)

# 간선 설정
graph = [ [] for i in range(people_num + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(t1, 0)
# print(count)
# print(family_list)
count_num = family_list.count(t2)
if len(family_list) == 0:
    print(-1)
else:
    print(family_list[0] - 1)