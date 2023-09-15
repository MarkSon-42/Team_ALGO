# 40min, time over code
def solution(routes):
	route_lst = [r for route in routes for r in range(route[0], route[1]+1)]
	route_lst = sorted(list(set(route_lst)))
	cameras = [False] * len(route_lst)

	cnt = 0
	for route in routes:
		is_there_camera = 0
		for r in range(route[0], route[1]+1):
			if cameras[route_lst.index(r)]:
				is_there_camera = 1
				break
		if not is_there_camera:
			for r in range(route[0], route[1]+1):
				cameras[route_lst.index(r)] = True
			cnt += 1

	return cnt
