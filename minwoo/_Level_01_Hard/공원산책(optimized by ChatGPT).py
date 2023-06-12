def solution(park, routes):
    answer = []

    # 'S'의 초기 위치를 찾습니다.
    for i in range(len(park)):
        if 'S' in park[i]:
            answer = [i, park[i].find('S')]
            break

    # 각 route에 대해 차량을 이동시킵니다.
    for route in routes:
        direction, move = route.split(' ')
        move = int(move)

        if direction == 'E':  # 동쪽으로 이동
            loc = answer[1] + move
            if loc < len(park[0]) and 'X' not in park[answer[0]][answer[1] + 1:loc + 1]:
                answer[1] = loc

        elif direction == 'W':  # 서쪽으로 이동
            loc = answer[1] - move
            if loc >= 0 and 'X' not in park[answer[0]][loc:answer[1]]:
                answer[1] = loc

        elif direction == 'S':  # 남쪽으로 이동
            loc = answer[0] + move
            if loc < len(park) and not any('X' in row[answer[1]] for row in park[answer[0] + 1:loc + 1]):
                answer[0] = loc

        elif direction == 'N':  # 북쪽으로 이동
            loc = answer[0] - move
            if loc >= 0 and not any('X' in row[answer[1]] for row in park[loc:answer[0]]):
                answer[0] = loc

    return answer
