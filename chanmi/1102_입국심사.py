def solution(n, times):
    # 입국 심사를 기다리는 사람 수 n
    # 한명을 심사하는데 걸리는 시간이 담긴 배열 times
    
    # 심사대 개수
    check_num = len(times)
    
    left = 1
    
    # right : 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 오래걸리는 사람에게 모두가 검사받음
    right = max(times) * n
    
    
    while left <= right:
        # mid : 모든 심사관들에게 주어진 시간
        mid = (left + right) // 2
        
        # people : 모든 심사관들이 mid분 동안 검사한 사람 수
        people = 0
        
        for time in times:
            people += mid // time
            if people >= n:
                break
                
        # 심사한 사람의 수가 n명보다 많을 경우(시간이 충분함)
        # [left, right]의 범위를 [left, mid - 1]로 변경 후 재탐색
        # = 심사에 필요한 시간을 더 줄일 수 있음
        if people >= n:
            answer = mid
            right = mid - 1
        
        # 심사한 사람의 수가 n명보다 적을 경우(검사 시간이 너무 부족함)
        # [left, right]의 범위를 [mid + 1, right]로 늘린다
        # = 심사에 필요한 시간을 전부 검사할 수 있을 때까지 늘리기
        elif people < n:
            left = mid + 1
            
    return answer
        
