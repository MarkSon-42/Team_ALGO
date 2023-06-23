def solution(n):
    answer = 0
    
    # 1. 일단 시초안날거같으니까 완탐해봄
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
    
    return answer