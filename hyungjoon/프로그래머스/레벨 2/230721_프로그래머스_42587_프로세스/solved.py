'''
문제 : 프로세스
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42587
'''
from collections import deque
def solution(priorities, location):
    answer = 0
    
    # 1. 그냥 for문 돌면 풀수는있는데, 더 효율적인거없나?
    q = deque()
    
    for idx, i in enumerate(priorities):
        q.append((idx, i))
        
    # 우선순위 비교하기 위해 얘도 덱으로 만들어줌
    priorities = deque(priorities)
        
    # 2. 조건에 맞게 pop해주다가, idx == location 이면 답 갱신해주고 return
    while q:
        ranking = max(priorities)
        temp1, temp2 = q.popleft(), priorities.popleft()
        idx, priority = temp1[0], temp1[1]
        # 여기서 우선순위 max를 뽑아내려고 priorities를 덱으로 만들었던거임
        if priority < ranking:
            q.append(temp1)
            priorities.append(temp2)
        # 현재 프로세스가 가장 높은 우선순위라면
        else:
            # 그리고 location과 동일하다면 break 해준다.
            if idx == location:
                answer += 1
                break
            else:
                answer += 1
                continue
    
    return answer
print(solution([1,1,1,2], 2))