def solution(brown, yellow):
    answer = []
    tmp_brown = brown - 4
    
    # tmp_brown : 네모의 가로 + 세로의 값
    tmp_brown = tmp_brown // 2
    
    # 노랑의 약수 구하기
    for i in range(1, yellow + 1):
        yellow_x = i
        yellow_y = yellow // yellow_x
    
        # 약수가 아닐 경우(나누어 떨어지지 않는 경우 continue)
        if yellow % i != 0:
            continue
            
        # 약수의 합이 tmp_brown과 일치할 경우 최종 길이 구하기
        if yellow_x + yellow_y == tmp_brown:
            
            # 이때 반드시 가로가 더 길어야함
            if yellow_x > yellow_y:
                return [yellow_x + 2, yellow_y + 2]
            else:
                return [yellow_y + 2, yellow_x + 2]
    
    
    return answer
