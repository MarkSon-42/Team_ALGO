# 상자의 크기가 주어질 때, 한 번에 넣을 수 있는 최대의 상자 개수

n = int(input())
box = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

# 상자에 넣는 방법이 여러가지인데 그 중에서 최대의 상자 개수를 출력해야 한다.

# 그러면 dp = max(dp[]~ 어쩌구) 이런 형태의 점화식일 가능성이 높다.

# 약간 이중반복문에서 dp를 쓰는 느낌..? 상자를 넣는것이 처음에 상자크기 주어진 순서에 영향을 받으므로

# dp[i] = max(dp[i], dp[j] + 1) (1 <= j < i) 이렇게 ㅇㅇ

# -> 이 문제 유형을 "최장 거리 부분 수열"이라고 하는듯..


for i in range(2, n + 1):
    for j in range(1, i):
        if box[i - 1] > box[j - 1]:
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            dp[i] = max(dp[i], 1)

print(max(dp))


#  https://jinho-study.tistory.com/1002

# 군더더기 1도 없는 다른사람의 깔끔한 코드


n = int(input())
li = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))