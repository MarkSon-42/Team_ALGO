# ref : https://dev-note-97.tistory.com/99

# 쉣.. 너무 어렵다

from itertools import permutations

def solution(numbers):
    nums = [n for n in numbers]
    per = [list(permutations(nums, i)) for i in range(1, len(numbers)+1)]
    new_nums = [int("".join(p)) for sublist in per for p in sublist]

    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    return len(set(filter(is_prime, new_nums)))
