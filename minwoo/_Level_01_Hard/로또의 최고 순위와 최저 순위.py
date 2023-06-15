# 우선 일치하는 것만 처리하면 그게 곧 최저순위이다.

# 여기서 0의 개수룰 더해주면 그게 최고 순위겠지.

# 순위를 어떻게 처리하나. -> 뒤집어야?
def solution(lottos, win_nums):
    answer = []
    min_order, max_order = 0, 0
    for i in range(6):
        if lottos[i] in win_nums:
            min_order += 1

        if lottos[i] == 0:
            max_order += 1
    return [min_order, min_order + max_order]