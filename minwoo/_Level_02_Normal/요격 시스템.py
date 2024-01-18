# 백준 2565랑 판박이임

def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))

    cut = -1
    answer = 0

    for left, right in targets:
        if left >= cut:
            answer += 1
            cut = right

    return answer


def solution2(targets):
    answer = 1
    targets.sort()

    s,e = targets[0]
    for target in targets[1:]:
        if target[0] < e:
            if target[1] < e:
                e = target[1]
            continue
        else:
            s, e = target
            answer += 1



    return answer
