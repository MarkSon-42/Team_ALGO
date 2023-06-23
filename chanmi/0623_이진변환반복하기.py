def solution(s):
    # 몇 번 이진변환했는지 저장하는 변수
    count = 0
    
    # 0을 몇 개 지웠는지 저장하는 변수
    delete_zero = 0

    
    while True:
        zero_index = s.find("0")
        # 입력값이 1로만 이루어진 경우
        if zero_index == -1:
            if s == "1":
                return [count, delete_zero]
            else:
                # 길이를 2진변환했을때 1111 등이 나온 경우
                count += 1
                
                # 길이를 bin()을 사용해 이진변환
                s_len = len(s)
                s = bin(s_len)
                s = str(s)
                s = s[2:]


        # 입력값이 0과 1로 이루어진 경우
        
        # 0은 지워주고
        zero_count = s.count("0")
        delete_zero += zero_count
        count += 1
        s = s.replace("0", "")
        
        # 길이를 bin()을 사용해 이진변환
        s_len = len(s)
        s = bin(s_len)
        s = str(s)
        s = s[2:]
    
    return answer