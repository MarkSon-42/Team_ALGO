import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input())
	rest = 1000 - N
	moneys = [500, 100, 50, 10, 5, 1]
	rst = 0

	for money in moneys:
		if rest == 0:
			break
		rst += rest//money
		rest %= money

	print(rst)