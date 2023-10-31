'''
문제 : 개똥벌레
난이도 : 골드 5
링크 : https://www.acmicpc.net/problem/3020
소요시간 : 
'''
import sys
import heapq
se = sys.stdin.readline
answer = 200001
min_answer = 0

n, h = map(int, se().split())
# 높이가 기준이 되어 투포인터를 진행
start, end = 0.5, h-0.5

arr = []
# 0은 석순, 1은 종유석
for i in range(n):
    if i % 2 == 1:
        arr.append([int(se().strip()), 1])
    else:
        arr.append([int(se().strip()), 0])

# 높이별로 개똥벌레를 발사시켜본다.
while start < end:
    start_sum, end_sum = 0, 0
    for i in arr:
        if (i[1] == 1 and i[0] > end) or (i[1] == 0 and i[0] > end):
            end_sum += 1
        if (i[1] == 0 and i[0] > start) or (i[1] == 1 and h - i[0] > start):
            start_sum += 1
    temp = min(start_sum, end_sum)
    if start_sum > end_sum:
        start += 1
    else:
        end -= 1
    if temp == answer:
        min_answer += 1
    answer = min(temp, answer)

print(answer)
print(min_answer)