# k = int(input())
# n = int(input())
# expect = input()
#
# # 사다리 입력 받기
#
# # 사다리 추적은 거꾸로 올라가면 된다 ? 그러나 이건 bfs나 dfs가 아니다.
#
# # 입코딩이라도
#
# # '*' '-' '?'을 판단
# # ?????????...?  -> 을 판단하려면
# # 그 직전 사다리 값을 알아야 할것인데
#
# # 그리고 사다리면 좌 우가 있어서 left, right
#
#
# for _ in range(n):
#     ladder = list(map(str, input().split()))
#     for i in range(k):
#
#


import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
# 마지막 모양과 처음 모양을 정해준다. 각 for 반복에 시작배열이 된다.
final = list(map(str, input().strip()))
start = sorted(final)

# left는 '??' 나오기 전까지의 사다리 모양을 넣어둔다.
# right는 '??' 나온 이후의 사다리 모양을 넣어둔다.
left = 0
right = []

for _ in range(m):
    ladder = list(map(str, input().strip()))

    # '??'이 나오면 현재까지의 right를 left에 넣고 right는 초기화
    # 분리하기 위한 방법이다.
    if ladder == ['?' for _ in range(n - 1)]:
        left = right
        right = []
        continue
    right.append(ladder)

# 처음상태(ABCDE~~)에서 '??'직전 배열을 알기 위한 코드이다.
# 앞에서 부터 하나씩 빼서 '-'이면 양 알파뱃의 위치를 바꾸어준다.
while left:
    ladder = left.pop(0)
    for i in range(n - 1):
        if ladder[i] == '-':
            start[i], start[i + 1] = start[i + 1], start[i]

        # 마지막상태에서 같은 방식으로 역순으로 해준다.
while right:
    ladder = right.pop()
    for j in range(n - 1):
        if ladder[j] == '-':
            final[j], final[j + 1] = final[j + 1], final[j]
# '??'인 부분의 초기상태를 *로 해준 후
# 자리를 바꾸어 같은 값이면 '*'을 '-'로 바꾸어준다.
ans = ['*' for _ in range(n - 1)]
for k in range(n - 1):
    if start[k] == final[k + 1] and start[k + 1] == final[k]:
        ans[k] = '-'
        start[k], start[k + 1] = start[k + 1], start[k]
# 바꾼 start와 final이 같으면 성공!
# 아니면 x를 출력한다.
if start != final:
    ans = ['x' for _ in range(n - 1)]
print(''.join(ans))