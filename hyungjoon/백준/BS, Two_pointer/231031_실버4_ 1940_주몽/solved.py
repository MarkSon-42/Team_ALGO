'''
문제 : 주몽
난이도 : 실버 4
링크 : https://www.acmicpc.net/problem/1940
소요시간 : 10분
'''
import sys
se = sys.stdin.readline

n = int(se().rstrip())
m = int(se().rstrip())
arr = list(map(int, se().split()))
arr.sort()
answer = 0

s, e = 0, n-1
while s < e:
    temp = arr[s] + arr[e]
    if temp > m:
        e -= 1
    elif temp < m:
        s += 1
    else:
        answer += 1
        s += 1
        e -= 1

print(answer)