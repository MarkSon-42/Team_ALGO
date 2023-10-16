import sys
my_input = sys.stdin.readline

# R: 뒤집기 함수
# D: 첫 번째 수 버리는 함수, 빈 배열 -> 에러 발생

T = int(my_input())

for _ in range(T):
	p = [c for c in my_input().rstrip()]
	n = int(my_input())
	arr = my_input().strip("[""]""\n").split(',')
	if n == 0:
		arr = []

	is_error = 0
	for inst in p:
		if inst == 'R':
			arr.reverse()
		else:  # inst == 'D'
			if len(arr) == 0:
				is_error = 1
				break
			del arr[0]

	if is_error == 1:
		print("error")
	else:
		print('['+','.join(arr)+']')