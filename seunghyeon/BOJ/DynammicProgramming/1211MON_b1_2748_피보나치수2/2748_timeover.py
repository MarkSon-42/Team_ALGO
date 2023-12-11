# 6 min, time over
import sys
my_input = sys.stdin.readline


def fibo(p_n):
	if p_n < 2:
		return p_n
	else:
		return fibo(p_n-1) + fibo(p_n-2)


n = int(my_input())
answer = fibo(n)
print(answer)
