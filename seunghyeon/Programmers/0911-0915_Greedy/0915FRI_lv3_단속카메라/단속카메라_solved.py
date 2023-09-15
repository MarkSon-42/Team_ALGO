def solution(routes):
	routes = sorted(routes, key=lambda x: x[1])
	key = -30001
	cnt = 0

	for route in routes:
		if route[0] > key:
			cnt += 1
			key = route[1]

	return cnt

# TIL
	# 너무 하나하나 풀어서 길게 생각하지 말자
	# 이런식으로 구간을 사용해야하는 경우, 구간을 펼쳐서 하나하나 비교하는 방법말고 시작점과 끝점을 활용할 방법을 생각해보자
	# 오름차순, 내림차순대롤 for문을 도는 경우 업데이트 해주는 값을 (맨 첫 값 -1) 또는 (마지막 값 + 1)로 초기화시켜주는 걸 먼저 생각해보자
