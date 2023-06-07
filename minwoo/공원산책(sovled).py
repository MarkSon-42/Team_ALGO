# 요즘.. 정말 많이나오는 brute force (완전탐색)... shxt....

# ref : https://windy7271.tistory.com/entry/PythonLV1%EA%B3%B5%EC%9B%90-%EC%82%B0%EC%B1%85
def solution(park, routes):
    answer = []
    for i in range(len(park)):
        if 'S' in park[i]:  # 'S'를 찾아서 초기 위치를 answer에 저장
            answer = [i, park[i].find('S')]  # find() : 문자를 찾아서 해당 위치의 index 반환 - 해당 문제에서는 인덱스로 위치를 처리하므로 find()가 유용하다.
            break

    for route in routes:
        direction, move = route.split(' ')  # routes가 방향과 거리를 문자열로 주기 때문이 값을 분리해준다.
        move = int(move)  # 거리는 숫자로 처리하기 위해 int()로 캐스팅.

        if direction == 'E':  # 동쪽(오른쪽)으로 이동시 조건 처리
            loc = answer[1] + move  # 현재 위치에서 이동거리만큼 오른쪽으로 이동한 위치(loc)를 계산
            if loc >= len(park[0]):  # 이동한 위치가 공원의 범위를 벗어나면 다음 route로 넘어감 (continue)
                continue
            if 'X' in park[answer[0]][answer[1]+1:loc+1]:
                # 현재 위치(answer[0] 행)와 이동한 위치 (answer[1] + 1부터 loc + 1까지) 사이에 'X'가 있는지 체크
                continue
            else:
                answer[1] = loc  # 공원의 범위를 벗어나지 않고, 진행 경로에 'X'가 걸리지 않는 경우에는 이동

        elif direction == 'W':  # 서쪽(왼쪽)으로 이동
            loc = answer[1] - move  # 현재 위치에서 이동거리만큼 왼쪽으로 이동한 위치(loc)를 계산
            if loc < 0:
                continue
            if 'X' in park[answer[0]][loc:answer[1]]:
                # 현재 위치 answer[0] 행에서      이동한 위치 loc 열부터 현재 위치 answer[1] 열까지 (왼쪽이기 때문에 역순)
                continue
            else:
                answer[1] = loc  # 생략

        elif direction == 'S':
            loc = answer[0] + move
            if loc >= len(park):
                continue
            # if 'X' in [park[i][answer[1]] for i in range(answer[0] + 1, loc + 1)]:
            #     continue
            obstacles = []  # 이동 범위에 장애물 'X'가 있는지 판별하기 위해 변수 선언
            for i in range(answer[0] + 1, loc + 1):  # 이동한 범위만큼
                obstacles.append(park[i][answer[1]])  # 장애물 판별 배열에 추가하기

            if 'X' in obstacles:  # 'X'가 있다면 다음 route
                continue

            else:
                answer[0] = loc

        elif direction == 'N':
            loc = answer[0] - move
            if loc < 0:
                continue
            # if 'X' in [park[i][answer[1]] for i in range(loc, answer[0])]:
            #     continue
            obstacles = []
            for i in range(loc, answer[0]):
                obstacles.append(park[i][answer[1]])
            if 'X' in obstacles:
                continue
            else:
                answer[0] = loc
    return answer