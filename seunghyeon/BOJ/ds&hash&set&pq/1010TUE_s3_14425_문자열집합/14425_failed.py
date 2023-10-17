# 문제 이해를 잘못해서 풀이 자체가 잘못된 코드

import sys
my_input = sys.stdin.readline


n, m = map(int, my_input().split())
s_words = set([my_input().rstrip() for _ in range(n)])
target_words = [my_input().rstrip() for _ in range(m)]

print(s_words.intersection(target_words))
