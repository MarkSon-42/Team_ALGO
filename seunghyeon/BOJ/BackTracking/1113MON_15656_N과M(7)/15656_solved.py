import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())
nums = sorted(list(map(int, my_input().split())))
tmp = []


def dfs():
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(n):
            tmp.append(nums[i])
            dfs()
            tmp.pop()

dfs()