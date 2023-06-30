'''
문제 : 구명보트
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42885
'''
def solution(people, limit):
    answer = 0
    
    # 정렬을 해서.. 가장 무거운사람 + 가장 가벼운사람 해서 되면 pop, 안되면 무거운놈만 pop 해주자
    people.sort()
    while people:
        # 2명 이상이라면 아래 로직을 따른다.
        if len(people) >= 2:
            if people[0] + people[-1] > limit:
                # 제일 무거운놈만 탈출
                people.pop()
                answer += 1
            elif people[0] + people[-1] <= limit:
                # 제일 무거운놈 + 제일 가벼운놈 둘이 탈출
                people.pop(0)
                people.pop()
                answer += 1
        # 1명만 남았다면 걍 pop해주고 보트 추가해주기
        else:
            people.pop()
            answer += 1
    
    return answer