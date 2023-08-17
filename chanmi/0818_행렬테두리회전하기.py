def solution(rows, columns, queries):
    
    table = [[0]*(columns + 1) for i in range(rows + 1)]
    count = 1
    answer = []
    
    # 인덱싱을 편하게 하기 위해 좌표를 1부터 시작하고 1 더 늘려서 넣어줌
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            table[i][j] = count
            count += 1
    for query in queries:
        
        # 각 좌표는 직사각형의 꼭짓점. 위치는 순서대로
        # x1     x2
        # x3     X4
        
        x1 = query[0]
        y1 = query[1]
        

        x4 = query[2]
        y4 = query[3]
        
        x2 = query[0]
        y2 = query[3]
        
        x3 = query[2]
        y3 = query[1]
        

        first_value = table[x1][y1]
        temp_value = -100
        value_list = [first_value]
        
        # x1->x2 : 위쪽 가로줄 옮기기
        for i in range(y1, y2):
            temp_value = table[x1][i + 1]
            table[x1][i + 1] = first_value
            first_value = temp_value
            value_list.append(first_value)
        
        # x2 -> x4 : 오른쪽 세로줄 옮기기
        for i in range(x2, x4):
            temp_value = table[i + 1][y4]
            table[i + 1][y4] = first_value
            first_value = temp_value
            value_list.append(first_value)
            
        
        # x4 -> x3 : 아래 가로줄 옮기기
        for i in range(y4, y3, -1):
            temp_value = table[x3][i - 1]
            table[x3][i - 1] = first_value
            first_value = temp_value
            value_list.append(first_value)
            
        # x3 -> x1 : 왼쪽 세로줄 옮기기
        for i in range(x3, x1, -1):
            temp_value = table[i - 1][y1]
            table[i - 1][y1] = first_value
            first_value = temp_value
            value_list.append(first_value)

        min_value = min(value_list)
        answer.append(min_value)
    
    return answer