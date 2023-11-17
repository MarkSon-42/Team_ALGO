# 15666

# 중복 체크해야함. -> set을 돌리는건 매우 낭비 같은데

# referenced  :  https://honggom.tistory.com/114

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
answer = []

def dfs(start):
    if len(answer) == m:
        for num in answer:
            print(num, end =' ')
        print()
        return

    dup = 0

# 수열 중복 방지에
    # start, dup을 사용

    for i in range(start, n):
        if dup != arr[i]:
            answer.append(arr[i])
            dup = arr[i]
            dfs(i)
            answer.pop()

dfs(0)

