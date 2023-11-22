# 친구만 보는게 아니라
# 친구의 친구도 구해야 함...

# 그래프 길이가 2까지

# 그래프 문제들은.. 그러니까 노드가 대놓고 나오는 경우
# 1번 인덱스부터 시작함을 생각해라..  n + 1로 그래프와 방문 체크 배열을 초기화
# 그렇다면 어지간한 문제는 그냥 무조건 n + 1로 초기화 해도 무방하지 않나..?

#  https://great-park.tistory.com/109

# visited 를 길이를 어떻게 카운트 하나 했는데
# visited의 값을 누적합으로 해서 depth를 추출 1(본인) 2(친구) 3(친구의친구)

from collections import deque
n, m = map(int, input().split())
graph = [[0] * (n + 1) for i in range(n + 1)]

visited = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



def bfs(x):
    queue = deque([x])
    visited[x] = 1

    while queue:
        friend_num = queue.popleft()
        for people_num in graph[friend_num]:
            if visited[people_num] == 0:
                queue.append(people_num)
                visited[people_num] = visited[friend_num] + 1

def solve():
    bfs(1)
    answer = 0
    for i in range(2, n + 1):
        if 0 < visited[i] <= 3:
            answer += 1
    print(answer)

solve()
























# dict, set으로 하면 가장 빠른 풀이가 가능하고 함... 오
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
# res = dict()
# resSet = set()
#
# for _ in range(m):
#     key, item = map(int, input().split())
#     if key not in res:
#         res[key] = list()
#     if item not in res:
#         res[item] = list()
#     res[key].append(item)
#     res[item].append(key)
#
# for key in res[1]:
#     resSet.add(key)
#     if key not in res:
#         continue
#     else:
#         for item in res[key]:
#             resSet.add(item)
#
# print(len(resSet) - 1)
