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