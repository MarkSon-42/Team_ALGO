from collections import deque


def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        queue = deque(skill)
        whether = True # 이렇게 flag를 설정해두면 되는 일이였다...

        for s in tree:
            if s not in queue:
                continue
            else:
                if s == queue[0]:
                    queue.popleft()
                else:
                    whether = False
                    break
        if whether:
            answer += 1

    return answer