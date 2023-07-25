# 그냥 완탐 구현

# 순열을 몰라서.. ㅜㅜ 풀이 참고

# https://yuna0125.tistory.com/153

from itertools import permutations


def solution(k, dungeons):
    d_num = len(dungeons)
    answer = []

    for per in permutations(dungeons, d_num):
        limit = k
        cnt = 0

        for p in per:
            if limit >= p[0]:
                limit -= p[1]
                cnt += 1
        answer.append(cnt)

    return max(answer)