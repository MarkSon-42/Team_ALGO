from collections import deque

# 스킬의 순서거 어긋나면 break
# 스킬에 포함되지 않는것은 상관없음
# 스킬트리에 포함되지 않는 것들을 제외하고 접근하면 ?


def solution(skill, skill_trees):
    answer = 0
    skill = deque(skill)

    for i in range(len(skill_trees)):
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] not in skill:
                continue
            elif skill_trees[i][j] in skill and skill.popleft() != skill_trees[i][j]:
                break
            elif skill_trees[i][j] in skill and skill.popleft() == skill_trees[i][j]:
                skill.popleft()
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)

