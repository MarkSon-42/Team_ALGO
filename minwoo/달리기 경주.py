#  출처 : https://velog.io/@heyggun/4%EC%BD%941%ED%8C%8C-94.-LV-1.-%EB%8B%AC%EB%A6%AC%EA%B8%B0-%EA%B2%BD%EC%A3%BC

def solution(players, callings):
    player_dict = {p: i for i, p in enumerate(players)} #  리스트의 각 플레이어에 대해 인덱스와 함께 딕셔너리를 생성
    idx_dict = {i: p for i, p in enumerate(players)} #  인덱스와 함께 players 리스트의 각 플레이어를 매핑하는 딕셔너리를 생성

    for call in callings:
        cur_idx = player_dict[call]
        front_idx = cur_idx - 1

        cur_player = call
        front_player = idx_dict[front_idx]

        player_dict[cur_player], player_dict[front_player] = front_idx, cur_idx
        idx_dict[cur_idx], idx_dict[front_idx] = front_player, cur_player

    return list(idx_dict.values())


# 왜 딕셔너리로 해야 시간복잡도 문제를 해결할 수 있는지?

# 1. Python의 리스트는 동적 배열로 구현되어 있기 때문에 실제로는 O(N)의 복사 작업이 필요

# 2.players.index(i)의 시간 복잡도: players.index(i)는 i라는 값을 players
# 리스트에서 찾기 위해 리스트를 순회. 따라서 최악의 경우
# players 리스트의 모든 요소를 확인해야 하므로 시간 복잡도는 O(N)이됨.
# 이 연산이 callings 리스트의 모든 요소에 대해 반복되므로, 총 시간 복잡도는 O(N*M)

# gpt의 답변 요약:

# 딕셔너리를 사용하여 플레이어와 인덱스 간의 매핑을 효율적으로 수행하였고,
# 또한 인덱스 교환을 통해 플레이어의 순서를 업데이트.
# 이에 비해 현재 코드는 매번 players.index(i)를 사용하여 플레이어의 인덱스를 찾아야 하고, 리스트 요소 교환에 대한 비용도 더 큼.