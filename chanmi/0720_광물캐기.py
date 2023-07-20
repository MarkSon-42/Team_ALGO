def solution(picks, minerals):
    # picks = [dia, iron, stone]
    
    # 곡괭이별 피로도
    dia = [0]
    iron = [0]
    stone = [0]
    
    # 5개 카운트하는 숫자
    is_five = 0
    i = 0
    
    for mine in minerals:
        if is_five % 5 == 0:
            i += 1
            dia.append(0)
            iron.append(0)
            stone.append(0)
            
        if mine == "diamond":
            dia[i] += 1
            iron[i] += 5
            stone[i] += 25
            
        elif mine == "iron":
            dia[i] += 1
            iron[i] += 1
            stone[i] += 5
            
        elif mine == "stone":
            dia[i] += 1
            iron[i] += 1
            stone[i] += 1
        else:
            print("오류")
        is_five += 1
    
    result = 0
    
    dia.remove(0)
    iron.remove(0)
    stone.remove(0)
    # 튜플 변환
    for i in range(len(dia)):
        dia[i] = (i, dia[i])
        iron[i] = (i, iron[i])
        stone[i] = (i, stone[i])
    
    # 가장 피로도가 높은 곳부터 다이아 곡괭이 사용해주기
    stone.sort(key = lambda x:x[1], reverse=True)
    print(stone)
    
    
    # 최종 곡괭이 수
    total_mine = sum(picks)
    
    # 최대 노드 수
    max_mine = len(stone)
    
    # 복사해두기
    tmp_stone = stone
    
    # 만약 곡괭이수의 총합 < 노드수인 경우
    if total_mine < max_mine:
        for item in tmp_stone:
            if item[0] + 1 > total_mine:
                stone.remove(item)
    
    for item in stone:
        
        # 최대값의 인덱스
        index = item[0]
    
        if picks[0] > 0:
            picks[0] -= 1
            result += dia[index][1]

        elif picks[1] > 0:
            picks[1] -= 1
            result += iron[index][1]
        elif picks[2] > 0:
            picks[2] -= 1
            result += item[1]
        else:
            return result

    return result