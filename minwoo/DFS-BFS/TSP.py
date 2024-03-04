n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

depth = 0
result = float('inf')
sum = 0

visited = [False]*n

def dfs(depth, now, start):
    global sum, result
    if depth == n and now == start:
        result = min(result, sum)
        return
    for i in range(n):
        if not visited[i] and w[now][i] > 0:
            visited[i] = True
            sum += w[now][i]
            if sum <= result:
                dfs(depth + 1, i, start)
            visited[i] = False
            sum -= w[now][i]

dfs(0, 0, 0)

print(result)