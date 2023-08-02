def solution(land):
    max_result = []
    
    # 각 줄에서 내려갔을 때의 최댓값 계산
    for i in range(4):
        max_total = 0
        before_index = -1
        for j in range(len(land)):
            if j == 0:
                max_total += land[j][i]
                before_index = i
            else:
                tmp_max = -100
                tmp_index = -10
                for k in range(4):
                    if k == before_index:
                        continue
                    else:
                        if land[j][k] >= tmp_max:
                            tmp_max = land[j][k]
                            tmp_index = k
                max_total += tmp_max
                before_index = tmp_index
        max_result.append(max_total)
            
    return max(max_result)