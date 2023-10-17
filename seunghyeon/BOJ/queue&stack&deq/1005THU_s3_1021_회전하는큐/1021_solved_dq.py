from collections import deque
import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	n, m = map(int, my_input().split())
	dq = deque(list(i+1 for i in range(n)))
	nums = list(map(int, my_input().split()))

	cnt = 0
	for num in nums:
		pos = dq.index(num) + 1
		dq_len = len(dq)
		if pos == 1:
			dq.popleft()
		elif pos <= (dq_len + 1) // 2:
			dq.rotate(-(pos-1))
			cnt += pos-1
			dq.popleft()
		else:
			dq.rotate(dq_len-pos+1)
			cnt += dq_len-pos+1
			dq.popleft()

	print(cnt)
