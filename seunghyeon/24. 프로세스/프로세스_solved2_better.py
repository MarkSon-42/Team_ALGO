# 효율성, 가독성 좋은 다른 분의 풀이 공부

def solution(priorities, location):
    q = [(i, p) for i, p in enumerate(priorities)] # idx, 중요도
    rank = 0

    while 1:
        tmp = q.pop(0)
        if any(tmp[1] < i[1] for i in q):
            q.append(tmp)
        else:
            rank += 1
            if tmp[0] == location:
                return rank
