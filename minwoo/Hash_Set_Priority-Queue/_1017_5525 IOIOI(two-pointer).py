# 이해 아직 못함.
# 투포인터 풀이인데 복잡도는 비슷해 보이는데..????
# 동일하게 문자열 순회
# 뒤에 굳이 불필요한 탐색을 안하긴 할듯.

import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()
left, right = 0, 0
answer = 0


while right < M:
    if S[right:right + 3] == 'IOI':
        right += 2
        if right - left == 2 * N:
            answer += 1
            left += 2
    else:
        left = right = right + 1

print(answer)

#