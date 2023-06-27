def solution(n, words):
    answer = []
    person = 1
    stage = 1
    word_list = []
    
    for i in range(len(words)):
        # 처음 시작하는 경우
        if i == 0:
            person += 1
            word_list.append(words[i])
            
        else:
            # 만약 중복 단어인 경우
            if words[i] in word_list:
                return [person, stage]
            
            # 끝말잇기 이어짐(앞뒤 단어가 동일)
            if words[i - 1][-1] == words[i][0]:
                person += 1
                word_list.append(words[i])
            
            # 끝말잇기 실패(앞뒤 단어 불일치)
            else:
                return [person, stage]
            
            # 한 번 다 돈 경우(한 번씩 단어 다 말함)
            if person > n:
                person = 1
                stage += 1

    return [0, 0]