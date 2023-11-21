# c
# s while == t

# 1 . *= 2
# 2.  += 1

# 1번 발차기를 하느냐, 2번 발차기를 하느냐. ->  bfs?

# 1번 예제만 그래프를 그려봐도 bfs로 풀 수 있음을 알 수 있다.

from collections import deque
def bfs(x, y):
    q = deque()
    q.append([x, y, 0])

    while q:
        s, t, cnt = q.popleft()
        if s < t:
            q.append([s * 2, t + 3, cnt + 1])
            q.append([s + 1, t, cnt + 1])
        if s == t:
            print(cnt)
            break

c = int(input())
for _ in range(c):
    s, t = map(int, input().split())
    bfs(s, t)

# bfs 동작시 큐에 들어가고 나오는 순서 (3개씩 s, t, cnt)
#  queue : | 10 | 20 | 0 |  20 |  33 |  1  | 11 | 20 | 1 | 30 | 23 | 2 | 22 | 23 |2 | 23 | 23 | 3

# 통과는 되는데 시간이 꽤 걸리는 느낌..?

# 다른 코드 ( 거의 같음 근데 visited를 왜쓰는건지..?)

# from collections import deque
# t = int(input())
#
#
# for i in range(t):
#     a, b = map(int,input().split())
#     visited = [0] * (200)
#     q = deque()
#     q.append((a,b,0))
#     while q:
#         x, y, z = q.popleft() #A, B, 최소 연속 발차기 횟수
#
#         if x <= y:
#             q.append((x*2, y+3, z+1))
#             q.append((x+1, y, z+1))
#             if x == y:
#                 print(z)
#                 break




######   [이게 좀 정석인듯]   #####

from collections import deque

def main():
    S, T = map(int, input().split())
    Q = deque([(S, T, 0)])
    while Q:
        s, t, c = Q.popleft()
        if s==t: return c
        if s>t: continue
        Q.append((s*2, t+3, c+1))
        Q.append((s+1, t, c+1))

C = int(input())
for _ in range(C):
    print(main())