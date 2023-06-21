# 스테이지별로 실패율을 계산, 정렬해서 스테이지 반환

# 스테이지 , 실패율을 매핑해서, 스테이지만 정렬 반환하면 된다.

# 주석은 gpt에게 부탁함.

def solution(N, stages):
    failure_rate = []  # 스테이지별 실패율을 저장할 리스트
    total_users = len(stages)  # 전체 플레이어 수


    # 1부터 N까지의 스테이지에 대해 반복
    for stage in range(1, N + 1):
        if total_users == 0:
            # 플레이어가 없는 경우 해당 스테이지의 실패율은 0
            failure_rate.append((stage, 0))
            continue

        # 해당 스테이지에 도달하지 못한 플레이어 수를 세기
        not_cleared_users = stages.count(stage)

        # 실패율 계산 및 저장
        failure_rate.append((stage, not_cleared_users / total_users))
        # 해당 스테이지에 도달한 플레이어 수를 전체 플레이어 수에서 빼기
        total_users -= not_cleared_users
    # 실패율을 기준으로 내림차순으로 정렬
    failure_rate.sort(key=lambda x: x[1], reverse=True)

    # key 매개변수에 람다함수를 써서 정렬 기준을 설정했다.
    # lambda     x: x[1]은 리스트의 각 요소 x의 두번째 요소  x[1]를 반환함.
    # 이를테면, failure_rate = [(1, 1/8), (2, 3/8), (...), (....), (....)] 이런식으로
    # 그리고 내림차순으로 reverse = True

    # 정렬된 실패율을 기반으로 스테이지만 추출하여 반환
    answer = [stage[0] for stage in failure_rate]

    return answer
