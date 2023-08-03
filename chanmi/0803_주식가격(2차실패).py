def solution(prices):
    answer = []
    
    # 총 몇 초인지 기록
    time_length = len(prices)
    max_price = max(prices)
    min_price = min(prices)
    
    low_index = -100
    
    # 상승을 확인하기 위한 스택
    max_stack = []
    max_index_stack = []
    time_track = [-1] * time_length
    
    for i in range(time_length):
        # 스택이 비어있는 경우
        if len(max_stack) == 0:
            max_stack.append(prices[i])
            max_index_stack.append(i)
        else:
            # 상승세거나 유지인 경우
            if prices[i] >= max_stack[-1]:
                max_stack.append(prices[i])
                max_index_stack.append(i)
            # 하락하는 경우
            else:
                # print("현재 인덱스 :", i)
                # print("현재 스택 :", max_stack)
                max_stack.pop()
                while True:
                    if len(max_stack) == 0:
                        time_track[i - 1] = i - max_index_stack[-1]
                        max_index_stack.pop()
                        max_stack.append(prices[i])
                        max_index_stack.append(i)
                        break
                    if max_stack[-1] <= prices[i]:
                        # print(max_stack[-1])
                        time_track[max_index_stack[-1]] = i - max_index_stack[-1]
                        max_index_stack.pop()
                        max_stack.append(prices[i])
                        max_index_stack.append(i)
                        break
                    else:
                        time_track[max_index_stack[-1]] = i - max_index_stack[-1]
                        max_index_stack.pop()
                        max_stack.pop()
    
    for i in range(time_length):
        if time_track[i] == -1:
            time_track[i] = time_length - i - 1
            
    # print(time_track)
    return time_track