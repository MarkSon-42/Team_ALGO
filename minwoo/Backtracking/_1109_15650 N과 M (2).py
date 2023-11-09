########################################################
########              백트래킹 기본 코드             ########
########################################################

# for i in range(1, n + 1):
#     if visited[i]:
#         continue
#
# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(1, n + 1):
#         if visited[i]:
#             continue
#         visited[i] = True
#         s.append(i)
#         dfs()
#         s.pop()
#         visited[i] = False


n, m = map(int, input().split())
s = []
visited = [False] * (n + 1)

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(i + 1)
        s.pop()
        visited[i] = False


dfs(1)