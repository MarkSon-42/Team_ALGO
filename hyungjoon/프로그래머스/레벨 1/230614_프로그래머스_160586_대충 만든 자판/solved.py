'''
문제 : 대충 만든 자판
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/160586
'''
def solution(keymap, targets):
    answer = []
    # 문자 : 가장빠른 숫자 순으로 맵을 만들어서 비교를 해볼까..?
    wordDic = {}
    
    # 1.keymap을 돌면서, dic 안에 해당 문자가 있으면 더 낮은수로 들어가게끔 해준다.
    
    for i in keymap:
        for j, word in enumerate(i):
            if word not in wordDic:
                # 1-1. n번 눌러야 되니까 +1 해주자
                wordDic[word] = j+1
            else:
                wordDic[word] = min(j+1, wordDic[word])
    
    # # 2. targets에 맞는 수를 가져와서 더해준다.
    # 이거 왜안됨?
    # for i in targets:
    #     temp = 0
    #     for j in i:
    #         if j in wordDic:
    #             temp += wordDic[j]
    #     # 2-1. 만약 만들 수 없는 수라면 -1 로 표현
    #     if temp == 0:
    #         temp = -1
    #     answer.append(temp)

    # 2. targets에 맞는 수를 가져와서 더해준다.
    for i in targets:
        temp = 0
        for j in i:
            # 2-1. 만약 만들 수 없는 수라면 -1 로 표현
            if j not in wordDic:
                temp = -1
                break
            temp += wordDic[j]
        answer.append(temp)
    
    return answer

solution(["AA"],["AB"])