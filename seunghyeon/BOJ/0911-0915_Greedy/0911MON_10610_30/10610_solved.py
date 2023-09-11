import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	number = list(my_input())
	number.sort(reverse=True)
	sum = 0
	for i in number:
		sum += int(i)
	if "0" not in number or sum % 3 != 0:
		print(-1)
	else:
		print("".join(number))
