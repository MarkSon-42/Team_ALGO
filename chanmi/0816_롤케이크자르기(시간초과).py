def solution(topping):
    
    # greedy식 해법으로 생각한 것 :
    # 인덱스로 하나씩 잘라서 set에 넣은 후 set의 길이를 비교하여 동일하면 공평한 것으로
    # 하지만 100만개를 다 잘라야 하므로 테스트 케이스는 통과해도 시간이 너무 오래 걸릴 것이라고 생각
    # -> 예상 적중함
    count = 0
    
    for i in range(1, len(topping)):
        first_piece = set(topping[:i])
        second_piece = set(topping[i:])
        if len(first_piece) == len(second_piece):
            count += 1
        
    return count