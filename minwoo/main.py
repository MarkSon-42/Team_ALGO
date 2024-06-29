from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    answer = []
    cnt = 0
    while True:
        if not progresses:
            break
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

            if progresses[i] >= 100:
                progresses.popleft()
                cnt += 1
            answer.append(cnt)
    return answer




print(solution([93, 30, 55], [1, 30, 5]))

