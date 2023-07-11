from collections import Counter
from functools import reduce

def solution(clothes):
    counter = Counter([type for clothes, type in clothes])
    answer = reduce(lambda typename, num: typename * (num + 1), counter.values(), 1) -1

    return answer
