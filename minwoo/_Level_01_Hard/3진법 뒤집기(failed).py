# ... 3**i 를 만족하는 가장 큰 i값을 우선 찾아야?

# 전혀 접근을 못하겠..
import math


def solution(n):
    answer = 0
    for i in range(sqrt(n)):
        if 3 ** i < n:
            continue

        if 3 ** i > n:

    return answer