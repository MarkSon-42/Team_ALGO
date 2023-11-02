# 이게 어떻게 이분탐색..

# 걸리는 시간을 최소로

# 나무 자르기에서는

# log_sum = i - mid이 최대로 되게끔 하였음

# 이해하기 쉬운 설명 : https://jie0025.tistory.com/204

def solution(n, times):
    # 모든 사람이 심사를 받는데 걸리는 총 시간 중 최소값?
    # 그 말인 즉슨.. lo up 경계에서 처음으로 나오는 가장 작은 값...?
    lower_bound, upper_bound = 1, 1_000_000_000  # ub : 1e9
    while lower_bound < upper_bound:
        answer = 0
        mid = (lower_bound + upper_bound) // 2
        for t in times:
            pass





    return answer