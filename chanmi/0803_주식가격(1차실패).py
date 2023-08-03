def solution(prices):
    answer = []
    
    # 총 몇 초인지 기록
    time_length = len(prices)
    max_price = max(prices)
    min_price = min(prices)
    
    low_index = -100
    
    # 상승을 확인하기 위한 스택
    max_stack = []
    time_track = [0] * time_length
    
    for i in range(time_length):
        # 현재가 저점인 경우
        if prices[i] <= min_price:
            time_track[i] = time_length - i - 1
            low_index = i
            
        # 현재가 저점이 아닌 경우
        else:
            # 아직 저점을 못 만난 경우(곧 떨어질 예정)
            if low_index == -100:
                j = 1
                find_index = -100
                while True:
                    if prices[i] - j <= 0:
                        break
                    try:
                        find_index = prices.index(prices[i] - j, i + 1)
                    except:
                        continue
                    if find_index != -100:
                        break
                    else:
                        j += 1
                time_track[i] = find_index - i
            # 이미 저점이 지나간 경우
            else:
                j = 1
                find_index = -100
                while True:
                    if prices[i] - j <= 0:
                        break
                    try:
                        find_index = prices.index(prices[i] - j, i + 1)
                    except:
                        find_index = -100
                    if find_index != -100:
                        break
                    else:
                        j += 1
                if find_index != -100:
                    time_track[i] = find_index - i
                else:
                    time_track[i] = time_length - i - 1
                
    
    return time_track