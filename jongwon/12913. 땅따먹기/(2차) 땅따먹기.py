def solution(land):
    N = len(land)
    highest_land = [[0]*4 for i in range(N)] # 첫 번째 줄
    depth = 1 # 두 번째 줄부터 시작

    # highest_land를 각 위치에서 가능한 최댓값으로 채우기 
    while depth < N: # highest_land의 마지막 줄에 다다를 때까지 이를 반복하고, 마지막 줄에 도달하면 while문을 종료
        for idx, val in enumerate(land[depth]):
            # 연속해서 같은 열은 방문 할 수 없게 조건문 걸어서 가능한 idx 생성
            possible_idx = [i for i in [0,1,2,3] if i != idx]

            max_val = 0
            for i in possible_idx:
                val = highest_land[depth-1][i] + land[depth-1][i]
                if max_val < val:
                    max_val = val 

            highest_land[depth][idx] = max_val

        depth += 1

    # highest_land의 마지막 줄의 값들을 각각 해당하는 값과 더해 최댓값을 반환 
    return max([a+b for a,b in zip(highest_land[-1], land[-1])])