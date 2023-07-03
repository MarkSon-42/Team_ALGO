'''
문제 : 귤 고르기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/138476
'''

def solution(k, tangerine):
    answer = 0
    
    # 1. 크기별로 몇개가 들어있는지 dic을 만들어준다.
    tanDic = {}
    for i in tangerine:
        if i not in tanDic:
            tanDic[i] = 1
        else:
            tanDic[i] += 1
    
    # 2. 문제 이해를 잘못함. 종류의 수가 최소인 경우를 다 알 필요가 없다. 그냥 최소인 케이스가 나오면 그거 return 해주면됨.
    # 따라서 내림차순 정렬해주고, k개 이상 담아버리는 순간 return 해주자
    tanDic = sorted(tanDic.items(), key=lambda x:x[1], reverse=True)

    for key, value in tanDic:
        if k == 0:
            break
        k -= value
        answer += 1

    print(answer)
    
    return answer

solution(6, [1, 3, 2, 5, 4, 5, 2, 3])