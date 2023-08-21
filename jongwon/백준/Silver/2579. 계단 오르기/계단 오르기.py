# 피보나치 수열 정리(DP 3단계 방법 : 재귀 -> Top-down -> Bottom-up 이러한 단계로 진행)
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


N = int(input())
stairs = [0]
dp_table = [0] * (N+1)

for j in range(1,N+1):
    stairs.append(int(input()))
    if j == 1 :
        dp_table[1] = stairs[1]
    elif j == 2 :
        dp_table[2] = stairs[1] + stairs[2]
    else:
        dp_table[j] = max(stairs[j] + stairs[j-1] + dp_table[j-3], stairs[j] + dp_table[j-2])

print(dp_table[N])

#제일 조심해야 할 조건은 연속된 3칸을 밟으면 안되기 때문에 트리 형태로 한 칸밟을때의 경우, 두 칸 밟을 때의 경우 ... 도착까지 그려 봤더니, \
# 일단 1칸더 올라가거나, 2칸 올라갈때를 나눠야 하고, 연속 3칸 경우를 방지 하기 위해 한 칸 : stairs[j] + stairs[j-1] + dp_table[j-3], 
# 두 칸 : stairs[j] + dp_table[j-2] 이렇게 경우를 나눠 주었다. 그래서 dp table에 각 경우의 점수를 더한 결과를 저장하고 max로 큰 값만 
# 저장 될 수 있도록 하였다. 마지막 도착지에서의 dp table에 누적된 칸의 점수 합을 반환하였다.
