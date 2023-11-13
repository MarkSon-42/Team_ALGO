n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []

def dfs(cnt):
    if cnt == m:
        for elem in answer:
            print(elem, end=' ')
        print()
        return

    for i in range(n):
        answer.append(arr[i])
        dfs(cnt + 1)
        answer.pop()

dfs(0)