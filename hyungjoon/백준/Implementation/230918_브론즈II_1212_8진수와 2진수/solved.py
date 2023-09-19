'''
문제 : 8진수와 2진수
링크 : https://www.acmicpc.net/problem/1212
소요시간 : 
'''
import sys
se = sys.stdin.readline

n = list(input())
answer = []

dec = int(n[-1])
mul = 1
for i in range(len(n)-2, -1, -1):
    dec += int(n[i]) * (8 ** mul)
    mul += 1

while dec != 1:
    answer.append(str(dec % 2))
    dec //= 2

answer.append(str(1))
print(''.join(answer[::-1]))
