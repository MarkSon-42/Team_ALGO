# # umm... 이 문제는 bfs,dfs랑 뭔상관이지
# # dfs로 가나?
#
# # 연결을 끝까지 했을때, 처음 수가 나오면 그것은 사이클이 있는 그래프임..!
#
# def dfs(arr):
#     global cnt
#     for i in range(1, len(arr) + 1):
#         for j in range(len(arr)):
#             arr[j] = i
#
#
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
