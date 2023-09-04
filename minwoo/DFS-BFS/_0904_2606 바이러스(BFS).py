from collections import deque
N = int(input())
M = int(input())

#  True False대신 1, 0 으로 초기화 하는 방법

pc = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    pc[a][b] = 1
    pc[b][a] = 1
visited = [0] * (N + 1)

q = deque()
q.append(1)

visited[1] = 1
cnt = 0
while q:
    current = q.popleft()
    if pc[current][i] == 1 and visited[i] == 0:
        #  "연결되어 있고 방문한 적 없으면"
        visited[i] = 1
        q.append(i)
        cnt += 1


print(cnt)
