import sys
my_input = sys.stdin.readline

n = int(my_input())

arr = []
arr.append(0)
arr.append(1)
arr.append(2)

if n >= 3:
	for i in range(3, n+1):
		arr.append(arr[i-2]+arr[i-1])

print(arr[n] % 10007)
