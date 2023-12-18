# n = int(input())

# 6

# SK

# 완벽하게 게임을 했을 떄 .. .?

# 1 4 1

# 4 1 1

# 1 4 1

# 5

# 1 3 1
# 3 1 1
# ...


# 7
# 4 3
# 3 4
# 1 3 3 ... ?
# 3 3 1

# dp[n] =


# https://eunsun-zizone-zzang.tistory.com/86

# 아니 n = 1, 2, 3... 부터 규칙성을 찾아봐야 하는데
# 아무 근거도 없이 6부터 시작해서 높은수들을 적으면서 찾으려니까
# dp초기값도 못찾고 규칙도 못찾고..

n = int(input())
# dp = []
# dp[1] = 1
# dp[2] = 1
# dp[3] = 0
# dp[4] = 1
# dp[5] = 1
dp = [1, 1, 0, 1, 1]
for i in range(5, n + 1):
    if dp[i - 1] + dp[i - 3] + dp[i - 4] == 3:
        dp.append(0)
        # python의 경우 append()도 그냥 O(1)
        # c++처럼 array alloc같은게 있다면, 초기화 없이 추가(삽입)하면 O(N)
    else:
        dp.append(1)

if dp[n] == 1:
    print("SK")
else:
    print("CY")
