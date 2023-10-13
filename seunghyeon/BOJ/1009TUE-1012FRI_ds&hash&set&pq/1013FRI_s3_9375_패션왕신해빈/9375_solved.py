from collections import Counter
import sys
my_input = sys.stdin.readline

testcase = int(my_input())
for _ in range(testcase):
	n = int(my_input())
	wearables = []
	for _ in range(n):
		a, b = my_input().split()
		wearables.append(b)

	wearables_counter = Counter(wearables)
	cnt = 1
	for wc in wearables_counter:
		cnt *= wearables_counter[wc] + 1

	print(cnt - 1)
