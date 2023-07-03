from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    sortdic = sorted(counter.items(), key = lambda x:-x[1])
    cnt = 0
    for i in sortdic:
        k -= i[1]
        answer += 1
        if k <= 0: break
        
    return answer
