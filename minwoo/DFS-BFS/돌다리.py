import sys
input = sys.stdin.readline

a, b, n, m = map(int, input().split())

stone_bridge = [0 for _ in range(100001)]
visited = [0 for _ in range(100001)]

ways = [1, -1, -a, a, -b, b, a, b]

q = []

def bfs(start):
    q.append(start)
    visited[start] = 1

    while q:
        x = q[0]
        del q[0]

        for i in range(8):
            if i < 6:
                nx = x + ways[i]

                if 0 <= nx < 100001 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    stone_bridge[nx] = stone_bridge[x] + 1

            else:
                nx = x * ways[i]

                if 0 <= nx < 100001 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    stone_bridge[nx] = stone_bridge[x] + 1

bfs(n)

print(stone_bridge(n))