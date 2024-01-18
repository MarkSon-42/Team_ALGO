# 4 ≤ numbers의 길이 ≤ 1,000,000
# 1 ≤ numbers[i] ≤ 1,000,000

# 다른건 모르겠고, 파라미터 길이 100만 -> 2중 쓰면 100,000,000,000 시간초과가 확실함
# 효율적인 자료구조, 알고리즘이 필요할 것.
# 딱히 떠오르는게 없는데? 이분탐색??
# 이분탐색을 하면 NlongN 잡히는건가

def solution(numbers):
    answer = []
    left, right = 0, len(numbers) - 1
    mid = 2 // len(numbers)

    while left < right:
        if numbers[mid] < numbers[left]:
            right = mid - 1
        else:

    return answer

