# 요즘.. 정말 많이나오는 brute force (완전탐색)... shxt....

# ref : https://windy7271.tistory.com/entry/PythonLV1%EA%B3%B5%EC%9B%90-%EC%82%B0%EC%B1%85
def solution(park, routes):

    answer = []
    for i in range(len(park)):
        if 'S' in park[i]:
            answer = [i, park[i].find('S')]
            break

    for route in routes:
        direction, move = route.split(' ')
        move = int(move)

        if direction == 'E':
            loc = answer[1] + move
            if loc >= len(park[0]):
                continue
            if 'X' in park[answer[0]][answer[1] + 1:loc + 1]:
                continue
            else:
                answer[1] = loc

        elif direction == 'W':
            loc = answer[1] - move
            if loc < 0:
                continue
            if 'X' in park[answer[0]][loc:answer[1]]:
                continue
            else:
                answer[1] = loc

        elif direction == 'S':
            loc = answer[0] + move
            if loc >= len(park):
                continue
            if 'X' in [park[i][answer[1]] for i in range(answer[0] + 1, loc + 1)]:
                continue
            else:
                answer[0] = loc

        elif direction == 'N':
            loc = answer[0] - move
            if loc < 0:
                continue
            if 'X' in [park[i][answer[1]] for i in range(loc, answer[0])]:
                continue
            else:
                answer[0] = loc

    return answer