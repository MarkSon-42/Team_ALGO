# 각 보석은 m가지 서로 다른 색상

# n명에게 모두 남김없이 나누어 주고

# 질투심 : 가장 많은 보석을 가져간 학생이 가지고 있는 보석 개수

# 질투심이 최소가 되게끔

# RRRR, BBBBBBB

# 5명, 2종류 4개 7개.

# -> RR, RR, BB, BB, BBB
# 적은것부터 가능한 균일하게 나누어 준다?
# 정렬해야함.

# 최소가 된다? -> mid를 설정하고 찾아가야 할듯

# 최소가 되어야 하는 값 : (전채 보석 갯수 // 아이들 수) + 나머지

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
gems = [int(input()) for _ in range(m)]
gems.sort()
sum_gems = sum(gems)
print(n, m, gems)
# 투포인터 인덱스 설정
i, j = 0, n - 1

while i < j:
    answer = (sum_gems // m) + (sum_gems % m)
    mid = (i + j) // 2
    if answer:
        pass

#  아님 아님.. 다시생각