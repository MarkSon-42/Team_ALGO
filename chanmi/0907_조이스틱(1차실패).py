def solution(name):
    # 'A' = 65
    # 'Z' = 90
    
    # 왼쪽, 혹은 오른쪽으로 움직였을 때 A가 가장 마지막에 오도록 하는게 최소
    left_name = name[0] + name[-1:0:-1]
    right_name = name
    

    # 오른쪽으로 쭉 움직일때 A 확인(count 함수를 써서 A가 없는 경우 세지 않음)
    while right_name.count('A'):
        # 맨 끝에 A가 있는지 확인, 없으면 지우지 않음
        if right_name[-1] == 'A':
            right_name = right_name[:-1]
        else:
            break
            
    # 왼쪽으로 쭉 움직일 때 A 확인(count 함수를 써서 A가 없는 경우 세지 않음)
    while left_name.count('A'):
        # 맨 끝에 A가 있는지 확인, 없으면 지우지 않음
        if left_name[-1] == 'A':
            left_name = left_name[:-1]
        else:
            break
    
    count = 0

    # 오른쪽으로 움직이는 게 이득인 경우
    if len(right_name) < len(left_name):
        for letter in right_name:
            if letter <= "N":
                count += ord(letter) - 65
            else:
                count += 91 - ord(letter)
        count += len(right_name) - 1
    else:
        for letter in left_name:
            if letter <= "N":
                count += ord(letter) - 65
            else:
                count += 91 - ord(letter)
        count += len(left_name) - 1
    
    if count == -1:
        count += 1
        
    return count