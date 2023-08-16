def solution(topping):
    
    # 딕셔너리를 이용해 토핑의 갯수를 저장
    count = 0
    
    # 토핑의 종류와 갯수를 저장할 딕셔너리형 변수 선언
    first_piece = {}
    second_piece = {}
    
    # first_piece 변수에는 topping의 모든 갯수를 저장
    for i in range(len(topping)):
        if topping[i] not in first_piece:
            first_piece[topping[i]] = 1
        else:
            first_piece[topping[i]] += 1
            
    
    for i in range(len(topping)):
        
        # 앞에서부터 하나씩 자르며 second_piece 변수에 topping의 종류와 갯수를 저장하며
        if topping[i] not in second_piece:
            second_piece[topping[i]] = 1
        else:
            second_piece[topping[i]] += 1
            
        # 저장할 때마다 first_piece에서 갯수를 하나씩 빼줌    
        if topping[i] in first_piece:
            first_piece[topping[i]] -= 1
        
        # 만약 first_piece에서 토핑의 갯수가 0개가 되면 len으로 비교하기 편하도록 해당 토핑을 지워줌
        if first_piece[topping[i]] == 0:
            del first_piece[topping[i]]
        
        if len(second_piece) == len(first_piece):
            count += 1
        
    return count