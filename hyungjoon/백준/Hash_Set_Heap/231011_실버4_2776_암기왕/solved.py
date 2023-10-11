'''
문제 : 암기왕
난이도 : 실버 4
링크 : https://www.acmicpc.net/problem/2776
소요시간 : 30분
'''
import sys

se = sys.stdin.readline

t = int(se())
for _ in range(t):
    n = int(se())
    set1 = set(map(int, se().split()))

    m = int(se())
    s = list(map(int, se().split()))

    for j in set1:
        if j in set1:
            print(1)
        else:
            print(0)