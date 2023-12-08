# 1, 2번 조건은 1926 그림문제와 유사하다. ( 거의 같다 )

# 그런데 3번 조건

# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

# 벽 제거 후 제일 큰 방 크기는.. 완탐으로 구하나?

# 다행스럽게도 성곽 범위는 M * N이다.

# 그리고 비트 활용을 하라는 힌트를 문제 말미에 주었다...

# 비트 활용이라니.. 비트마스킹을 써야하나?

# 비트마스킹을 쓰면 어떤 장점이 있을까?

# 비트마스킹을 쓰면 메모리를 아낄 수 있다.

# 비트마스킹을 쓰면 연산 속도가 빨라진다.

# 비트마스킹을 쓰면 코드가 간결해진다.



from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 1. 방의 개수
room_count = 0

# 2. 가장 넓은 방의 넓이
max_room = 0

# 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
max_room_removed = 0

def bfs(x, y, ):
    pass

