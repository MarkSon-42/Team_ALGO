import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N, M = map(int, my_input().split())

	if N == 1:
		print(1)
	elif N == 2:
		print(min(4, (M+1)//2))
	elif M <= 6:
		print(min(4, M))
	else:
		print(M-2)

# 이 문제의 코드자체는 매우 간단. 문제를 잘 이해하고 규칙을 찾는 힘을 더 기르자!