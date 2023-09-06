# dfs

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        count = 1  # 현재 집을 카운트
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            count += dfs(nx, ny)  # 인접한 집을 재귀적으로 카운트
        return count
    return 0


village_cnt = 0
houses = []

for j in range(n):
    for k in range(n):
        house_cnt = dfs(j, k)
        if house_cnt > 0:
            houses.append(house_cnt)
            village_cnt += 1

# 오름차순 정렬
houses.sort()
print(village_cnt)
for l in range(len(houses)):
    print(houses[l])



# dfs가 유리한 경우
# 1. 재귀적인 특징과 백트래킹을 이용하여 모든 경우를 하나씩 전부 탐색하는 경우
# 2. 그래프의 크기가 클 경우
# 3. 최적의 답을 찾는 것이 아닌 경우
# 4. 경로의 특징을 저장해야하는 경우 ex) 경로의 가중치, 이동 과정에서의 제약

# bfs가 유리한 경우
# 1. 최단 거리, 최단 횟수 구하는 경우
# 2. 최적의 답을 찾는 경우, bfs에서는 가장 처음 발견되는 답이 최단 거리
# 3. 탐색의 횟수를 구해야 하는 경우
