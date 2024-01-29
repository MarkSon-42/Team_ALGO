# https://school.programmers.co.kr/questions/46216

from collections import deque

def solution(pick_counts, mineral_types):
    total_tiredness = 0
    # 각 곡괭이별로 광물을 캤을 때의 피로도를 저장하는 2차원 테이블 정의
    tiredness_table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    # 광물의 종류를 인덱스로 변환하는 딕셔너리 정의
    mineral_index = {
        "diamond": 0,
        "iron": 1,
        "stone": 2,
    }
    # 각 광물 그룹별로 사용된 곡괭이의 피로도를 저장할 리스트 초기화
    tiredness_info = []

    # 광물의 종류를 곡괭이의 총 개수만큼만 잘라서 저장 ( 광물 남아도 곡괭이 다쓰면 못캐므로 )
    mineral_types = mineral_types[:5 * sum(pick_counts)]

    mineral_queue = deque(mineral_types)

    while mineral_queue:
        # 한 그룹당 캘 광물의 개수를 저장하는 변수 초기화
        dig_count = 0
        # 각 곡괭이별로 캔 광물에 대한 피로도를 저장하는 변수들 초기화
        dia_tiredness, iron_tiredness, stone_tiredness = 0, 0, 0

        # 한 그룹당 5개의 광물을 캐거나 광물이 더 이상 없을 때까지 반복
        while dig_count < 5 and mineral_queue:
            dig_count += 1
            current_mineral = mineral_queue.popleft()
            # 다이아몬드 곡갱이로 광물을 캤을 때의 피로도를 계산하여 diamond_tiredness에 더합니다.
            dia_tiredness += tiredness_table[0][mineral_index[current_mineral]]
            iron_tiredness += tiredness_table[1][mineral_index[current_mineral]]
            stone_tiredness += tiredness_table[2][mineral_index[current_mineral]]

            tiredness_info.append([dia_tiredness, iron_tiredness, stone_tiredness])
        tiredness_info.sort(key=lambda x: [x[2], x[1], x[0]])