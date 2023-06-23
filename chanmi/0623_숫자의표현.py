def solution(n):
    
    # 연속된 자연수의 합으로 숫자를 만들때, 해당 자연수는 최대값이 n/2 + 1만큼임
    # 예를 들어 15의 경우, 최대는 8 (<-7 + 8)

    max_n = int(n / 2)
    count = 1
    
    # brute force 방식으로 1부터 더해가며 찾음
    for i in range(max_n):
        result = 0
        j = i + 1
        while True:
            result += j
            
            # 커지면 종료
            if result > n:
                break
                
            # 같아지면 종료
            elif result == n:
                count += 1
                break
                
            # 아직 작을 경우 계속 더함
            else:
                j += 1
    answer = count
    return answer