def solution(s):
    first_num = s.count("(")
    second_num = s.count(")")
    
    # 괄호의 갯수가 다른 경우 당연히 닫히지 않음
    if first_num != second_num:
        return False
    
    else:
        
        # 앞이 )거나 뒤가 (인 경우에는 반드시 괄호가 닫히지 않음
        if s[0] == ")" or s[-1] == "(":
            return False
        
    
        else:
            find_index = -100
            
            # 여기서 시간복잡도가 증가하는 것 같은데 어떻게 찾아야할지 고민중... 큐나 스택 써보기?
            # 효율성 1번 빼고 전부 통과함
            while True:              
                find_index = s.find("()")
                if find_index == -1:
                    break
                else:
                    s = s.replace("()", "")
            if len(s) != 0:
                return False
            else:
                return True
    
        