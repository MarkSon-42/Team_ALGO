# 배열, dp 이용.

import sys
my_input = sys.stdin.readline

n = int(my_input())

fibo = []
fibo.append(0)
fibo.append(1)

if n >= 2:
	for i in range(2, n+1):
		fibo.append(fibo[i-2]+fibo[i-1])

print(fibo[n])
