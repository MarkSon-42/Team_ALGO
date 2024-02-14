# https://www.youtube.com/watch?v=m3kCKV8oc1g

# 숫자 조합
# 소수가 아닌 수 제거
# permutation?

from itertools import permutations
def solution(numbers):
    prime_set = set()

    # 1. 모든 숫자 조합 만들어보기
    for i in range(len(numbers)):
        # print(list(numbers))
        numbers_permutation = permutations(list(numbers), i + 1)
        # print(list(numbers_permutation))

        print(list(map("".join, numbers_permutation)))

    answer = 0
    return answer