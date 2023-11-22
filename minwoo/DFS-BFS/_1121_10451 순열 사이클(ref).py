# 풀이 1 : dfs 재귀

import sys
sys.setrecursionlimit(10000)



input = sys.stdin.readline

test_case = int(input())

def dfs(node):
    visited[node] = True
    next_node = tree[node]
    if not visited[next_node]:
        dfs(next_node)


for _ in range(test_case):
    N = int(input())
    tree = [0] + list(map(int, input().split()))
    # <- 0 index , 1 index주의 -> 이것때문에 분명히 다짰는데 계속 틀림   그래프 넘버가 1부터 시작하니 배열 인덱스를 조심..

    visited = [False] * (N+1)
    answer = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            answer += 1
    print(answer)




# 풀이 2 : dfs with stack  + 추후 풀이 예정..