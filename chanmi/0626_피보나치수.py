def solution(n):
    fib = [0, 1, 1]
    for i in range(3, n+1):
        fib.append(((fib[i -2] % 1234567) + (fib[i -1] % 1234567)) % 1234567)
    answer = fib[-1]
    return answer