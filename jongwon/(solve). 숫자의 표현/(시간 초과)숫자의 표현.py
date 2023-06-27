# 3중 반복문을 사용하여 시간 복잡도가 O(N^3)이라 시간 초과로 실패

def solution(n):
    nums = [num for num in range(1, n+1)]
    result = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            sum = 0
            while True:
                sum += nums[j]
                if sum == n:
                    result += 1
                    break
    
    return result