def solution(routes):
	unpacking_routes = sum(routes, [])
	route_lst = [r for r in range(min(unpacking_routes), max(unpacking_routes)+1)]
	cameras = [False] * len(route_lst)

	cnt = 0
	for route in routes:
		for r in range(route[0], route[1]+1):
			if not cameras[route_lst.index(r)]:
				cameras[route_lst.index(r)] = True
			else:
				cnt -= 1
				break
		cnt += 1

	return cnt



routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)