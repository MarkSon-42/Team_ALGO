def solution(land):
    answer = 0
    j = 0
    
    for item in land:
        # 각 행마다 enumerate를 이용해 index와 함께 묶어줌
        for inner_item in enumerate(item):
            item[inner_item[0]] = inner_item
        # 땅따먹기 점수가 큰 순서대로 각 행마다 내림차순 정렬
        item.sort(key = lambda x:x[1], reverse=True)
        land[j] = item
        j += 1
    
    max_total = 0
    before_index = -1
    
    # 최댓값 구하기
    for i in range(len(land)):  
        
        # 최대값의 인덱스가 이전과 겹치는 경우 그 다음으로 큰 숫자 입력
        if land[i][0][0] == before_index:
            max_ground = land[i][1][1]
            before_index = land[i][1][0]
            
        # 겹치지 않는 경우 0번째 원소 입력
        else:
            max_ground = land[i][0][1]
            before_index = land[i][0][0]
        max_total += max_ground
            
    return max_total