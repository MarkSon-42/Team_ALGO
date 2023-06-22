def solution(s):
    
    # isalpha() 함수를 사용하기 위해 임시로 공백 제거
    # isalpha() 함수를 통해 숫자가 들어가 있는지 아닌지 확인
    tmp_s = s.replace(" ", "")
    answer = ''
    
    # 만약 문장에 숫자가 없을 경우, title() 함수를 통해 JadenCase로 변경
    if tmp_s.isalpha():
        answer = s.title()
        return answer
    
    # 문장에 숫자가 있는 경우, 띄어쓰기를 기준으로 단어를 분리함
    else:
        word_list = s.split(" ")
        for i in range(len(word_list)):
            word = word_list[i]
            if word == "":
                answer += " "
            
            # 숫자로 시작하는 단어는 뒷부분을 그대로 진행
            elif "0" <= word[0] and word[0] <= "9":
                answer += word[0] + word[1:].lower() + " "
            
            # 숫자 이외의 단어는 전부 대문자로 시작하도록
            else:
                answer += word.title() + " "
        answer = answer[:-1]
        return answer