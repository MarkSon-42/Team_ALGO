# 문제는 bottom-up 방식으로 풀었는데 피보나치 문제가 DP 대표문제이므로 대표적인 방식 3가지로 다양하게 구현해봤습니다.

# Bottom-up 방식 (for loop 반복문 사용, 아래부터 위로 올려서 계산, basecase를 필두로 밑에서 부터 위로 올라가는 방식)
F = {0:0, 1:1} # 메모리 사용

def solution(n): # DP 중 bottom up 방식을 사용해서 딕셔너리에 F[0], F[1] 값을 넣어놓고 없는 value 값은 덧셈을 통해 딕셔너리에 추가하고 n까지 추가하는 방식
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n] % 1234567


# Top-down 방식 (재귀 방식, 위에서 부터 아래로 내려가는 방식), 추가 하면서 딕셔너리 채워 나가는 방식
F = {} # 메모리 사용
def solution(n):
    if n == 0: # basecase(탈출문)
        return 0
    elif n == 1:
        return 1
    if n not in F: # F 딕셔너리에 n 계산값이 없을 때
        F[n] = F(n-1) + F(n-2)
    return F[n] % 1234567

# 기본 재귀 방식
def solution(n): 
    if n == 0: # basecase(탈출문)
        return 0
    elif n == 1:
        return 1
    return (solution(n-1) + solution(n-2)) % 1234567 # 하위 문제로 나눠서 구하기




# 피보나치 수열

def fibo(n): 
    if n == 1 or n == 2: # base case
        return 1
    return fibo(n-1) + fibo(n-2) # 하위 문제로 나눠서 구하기

# f(7) = 1 1 2 3 5 8 = 13
# 시간 복잡도 : O(2^n)
# 중복되는 부분이 많아서 memoization을 사용하여 시간 복잡도를 O(n)으로 줄일수 있다.

# 딕셔너리 사용하여 memoization 사용해서 시간 복잡도를  O(n)으로 줄였다.
# Top-down 방식 (재귀 방식, 위에서 부터 아래로 내려가는 방식)
memo = {} # 메모리 사용
def fibo(n):
    if n == 1 or n == 2:
        return 1
    if n not in memo: # memo 딕셔너리에 n 계산값이 없을 때
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

# Bottom-up 방식 (for loop 반복문 사용, 아래부터 위로 올려서 계산, basecase를 필두로 밑에서 부터 위로 올라가는 방식)
memo = {1:1, 2:1} # 메모리 사용
def fibo(n):
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]