'''
문제 : 소가 길을 건너는 이유 1
링크 : https://www.acmicpc.net/problem/14467
소요시간 : 5분
'''
import sys
se = sys.stdin.readline

n = int(input())
cows = {}
cnt = 0

for _ in range(n):
    cow, num = map(int, se().strip().split())
    if cow in cows:
        if cows[cow] != num:
            cnt += 1
        cows[cow] = num
    else:
        cows[cow] = num

print(cnt)