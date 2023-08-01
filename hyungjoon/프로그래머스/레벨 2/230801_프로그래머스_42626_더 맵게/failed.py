'''
문제 : 더 맵게
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42626
'''
from collections import deque

def solution(scoville, K):
    answer = 0
    
    while True:
        # 만약, scoville 의 길이가 1인데 K 미만이면 -1 return 
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        # 1. 정렬을 해주고, 맨 앞 요소가 K 이상이면 정답 return
        scoville.sort()
        if scoville[0] >= K:
            return answer
        
        # 2. 섞어주기 진행
        scoville = deque(scoville)
        a, b = scoville.popleft(), scoville.popleft()
        scoville.appendleft(a + (b*2))
        scoville = list(scoville)
        answer += 1