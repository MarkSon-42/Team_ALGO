from collections import deque

def targetLocation(rst, location):
    for i in rst:
        if i[1] == location:
            return i[2]

def solution(priorities, location):
    q = deque()
    for i, p in enumerate(priorities):
        q.append((p, i, 0)) # p: 순위, i: 처음 인덱스

    rst = []
    rank = 0
    while q:
        maxVal = max(q[i][0] for i in range(len(q)))
        a, b, c, = q.popleft()
        if a < maxVal:
            q.append((a, b, c))
        else:
            rank += 1
            rst.append((a, b, rank))

    return targetLocation(rst, location)
    


# --------------------------
# targetLocation 함수 내용에 대한 다른 분의 코드 작성 방식
# def check(result, location):  
#     for _ in result:
#         a, b, c = _
#         if b == location:
#             return c
