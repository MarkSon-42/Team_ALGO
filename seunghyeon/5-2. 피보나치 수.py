def solution(n):
    fibo0, fibo1 = 0, 1
    answer = 0
    for i in range(2, n + 1):
        fibo0, fibo1 = fibo1, fibo0 + fibo1

    return fibo1 % 1234567
