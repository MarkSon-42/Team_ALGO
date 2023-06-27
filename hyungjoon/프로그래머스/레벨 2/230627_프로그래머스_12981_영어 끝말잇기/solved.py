'''
문제 : 영어 끝말잇기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12981
'''
def solution(n, words):
    answer = [0, 0]
    l = len(words)
    
    for i in range(1, l):
        # 몇번째 사람이 몇번 차례에 말했는지 정해주는 과정
        # 1. (특정 단어 인덱스 % 사람 수) + 1 한 값이 n번째 사람이 말한 단어이다.
        # ex) (5번째 단어 % 3) + 1 -> 2번째 사람이 말한것
        # 2. 마찬가지로 특정 단어 // 사람 수 한 값은 n번째 사람이 m번 차례에 말한 것.
        player = (i % n) + 1
        turn = i // n + 1
        # 3. 끝말잇기 조건이 성립하는지
        if words[i][0] == words[i-1][-1]:
            # 3-1. 이전에 나왔던 말인지 체크
            temp = words[:i]
            if words[i] not in temp:
                continue
            else:
                answer = [player, turn]
                break
        else:
            answer = [player, turn]
            break
    
    return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])