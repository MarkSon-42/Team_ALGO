def solution(s):
    while True:
        s_len = len(s)
        tmp_letter = s[0]
        sentence = ""
        is_find = False
        for i in range(1, s_len):
            if s[i] == tmp_letter:
                sentence = tmp_letter + s[i]
                is_find = True
                break
            else:
                tmp_letter = s[i]
        if is_find == True:
            s = s.replace(sentence, "")
            
            if len(s) == 0:
                return 1
        else:
            return 0
            

    return answer