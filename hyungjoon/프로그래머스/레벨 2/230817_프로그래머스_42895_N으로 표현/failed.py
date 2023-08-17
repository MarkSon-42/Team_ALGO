'''
문제 : N으로 표현
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42895
'''
def solution(N, number):    
    # N을 1부터 8번 썼을 때 집합을 모두 구해본다.
    # for문을 돌면서 해당 숫자가 있으면 정답 return, 없으면 -1
    
    # 5가 1번 들어간거 -> 5
    # 5가 2번 들어간거 -> 55, 5+5, 5-5, 5/5, 5*5
    # 5가 3번 들어간거 -> 555, 55+5, 55-5, 55/5, 55*5, (5+5)*5 <- 이런거 어케계산함?
    
    # n+1번 들어간거 계산하기 위해서는 n번까지 만든 데이터끼리 사칙연산을 해주면 된다!
    
    # 1. 각 인덱스마다 N을 n번 사용한 데이터가 set으로 들어간다.
    numlist = [[0]]
    # N이 1번 들어간거
    temp = set()
    temp.add(N)
    numlist.append(temp)
    
    if N == 1:
        return 1
    
    # N이 2번 들어간거
    temp = set()
    temp.add(int(str(N)*2))
    temp.add(N+N)
    temp.add(N-N)
    temp.add(N*N)
    temp.add(N//N)
    numlist.append(temp)
    
    if number in temp:
        return 2
    
    for i in range(3, 9):
        temp = set()
        # 1. 이어붙인거 하나
        temp.add(int(str(N)*i))
        # 2. i-1번째 숫자끼리 사칙연산
        for j in range(i):
            for a in numlist[j]:
                for b in numlist[j]:
                    if a == b:
                        continue
                    temp.add(a+b)
                    temp.add(a-b)
                    temp.add(a*b)
                    if b != 0:
                        temp.add(a//b)
                    
        if number in temp:
            return i
        numlist.append(temp)
    
    return -1
print(solution(5, 12))