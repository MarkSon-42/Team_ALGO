def solution(n):
    ans = 0
    
    while n:
        # 2진법 변환했는데 1이 있는 경우 ans를 1 증가
        if n % 2 == 1:
            ans += 1
        n //= 2
    
    return ans