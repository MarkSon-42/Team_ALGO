def solution(arr1, arr2):
	answer = []

	n = len(arr1)
	j = len(arr1[0])
	m = len(arr2[0])

	for s in range(n):
		mid = []
		for q in range(m):
			sum = 0;
			for r in range(j):
				sum += arr1[s][r] * arr2[r][q]
			mid.append(sum)
		answer.append(mid)

	return answer
