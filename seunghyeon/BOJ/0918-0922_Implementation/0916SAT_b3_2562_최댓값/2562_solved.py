import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	lst = []
	for _ in range(9):
		lst.append(int(my_input().rstrip()))
	max_num = max(lst)
	print(max(lst))
	print(lst.index(max_num)+1)
