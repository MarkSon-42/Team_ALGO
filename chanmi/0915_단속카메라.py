def solution(routes):
    routes.sort(key = lambda x : x[1])
    lasor = 1
    current_pos = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > current_pos:
            current_pos = routes[i][1]
            lasor += 1
    
    return lasor