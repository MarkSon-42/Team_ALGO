def solution(citations):
    citations.sort(reverse=True)
    hIdx = 0
    for i in citations:
        if i > hIdx: hIdx += 1
    return hIdx
