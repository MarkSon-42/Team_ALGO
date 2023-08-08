# 중복을 제거하고
# 범위 이탈을 제거하면 끝!
# 맵 사이즈도 5*5 고정
# 다만 칸에서 노는게 아니라 좌표선에서 움직이는 것임


def solution(dirs):
    answer = 0
    # 좌표평면의 시작위치 설정
    # map_arr = [[(0,0) for j in range(5)] for i in range(5)]
    road_list = []  # 지나간 길을 넣어주고 추후에 set()으로 중복처리할 것임
    loc = (0, 0)
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            loc = (loc[0] + 1, loc[1])
            road_list.append(loc)
        if dirs[i] == 'D':
            loc = (loc[0] - 1, loc[1])
            road_list.append(loc)
        if dirs[i] == 'L':
            loc = (loc[0], loc[1] - 1)
            road_list.append(loc)
        if dirs[i] == 'R':
            loc = (loc[0], loc[1] + 1)
            road_list.append(loc)

    return road_list  # 여기에 set()으로 중복 날리고, abs() > 6도 전부 쳐내면 됨.

# loc = (loc[0] + 1, loc[1])

# 이런 스파게티는 안짜느니만 못하다..좀 더 생각