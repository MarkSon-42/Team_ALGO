# ... 무슨 소리지

# D[1] = A

# D[N] = D[N-1]의 각 자리의 숫자를 p번 곱한 수들의 합 -> DFS ?

# A = 57

# 5^2 + 7^2 = 25 + 49 = 74  7^2 + 4^2 =  65  , ...

# ㅇㅎ. 그런데 숫자가 반복됨. 3^2 + 7^2 는 9 + 49 = 58

# 반복되는 부분을 제외..? 아하

# 37, 58, 89, .... 16, 37  -> 58, 89....

# silver 4????

# 그냥 구현 -> s4

# dfs -> s2~s1 인듯 ㅜㅜ

n, m = map(int, input().split())
check = [0] * 236197  # 9 ** 5 + 9 ** 5 + 9 ** 5 + 9 ** 5 최대 인덱스의 값이기 때문
iteration = 1


def cal(a, b):
    result = 0
    for i in str(a):
        result += pow(int(i), b)
    return result


def dfs(n, m, iteration, check):
    if check[n] != 0:
        return check[n] - 1

    check[n] = iteration
    iteration += 1
    result = cal(n, m)
    return dfs(result, m, iteration, check)


print(dfs(n, m, iteration, check))