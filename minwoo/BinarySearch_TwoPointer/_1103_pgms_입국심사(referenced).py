# 풀이 아이디어

# "mid를 사람들이 심사를 받는데 걸리는 총 시간으로 생각한다."

def solution(n, times):
    lower_bound, upper_bound = 1, max(times) * n  # n명을 검사하는데 최대로 많은 시간이 걸리려먼
    # 가장 오래걸리는 심사대에 n명이 다 검사받을 경우

    answer = upper_bound  # 최소값을 구하는 문제이기 때문에 구하는 값을 우선 가장 큰 값으로 초기화

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        people = 0
        for t in times:
            people += (mid // t)  # mid // t : 각 심사관이 mid라는 시간동안 심사할 수 있는 사람의 수 -> people에 더해서 n값과 비교

        if people < n:
            start = mid + 1
        else:
            upper_bound = mid - 1
            answer = min(answer, mid)

    return answer


# 아직도 완벽히 이해가 안가요....
