# 11053에서

# 출력만 조금 다른 문제..?

n = int(input())

arr = list(map(int, input().split()))
dp = [1] * (n + 1)  # 증가하는 부분 수열의 길이를 저장

for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

answer = max(dp)
print(answer)

# 10 20 30 50

# 여기서 요소를 출력하는 것만 추가 구현하면 된다??
# ... 어떻게????

# 무슨 수로 10 20 30 50을 찾아내서 출력할까.


seq = []

# 긴 수열 찾기

# https://mxxcode.tistory.com/58

for i in range(n - 1, -1, -1):
    if dp[i] == answer:  # 증가하는 최대 부분 수열 길이만큼 조건문에서 걸러질 것.
        seq.append(arr[i])
        answer -= 1  # 길이 하나 줄여주기

seq.reverse()

for i in seq:
    print(i, end = ' ')

# 왜
# 50 30 20 10으로 출력..?

# dp테이블 거꾸로 돌면서 검사

# 아니 이건.. 사실상 문제 로직 자체는 옛날에 풀었던 싸피문제랑 비슷한데

# 진짜 머리가 퇴화한거 아닌가..? 공부를

