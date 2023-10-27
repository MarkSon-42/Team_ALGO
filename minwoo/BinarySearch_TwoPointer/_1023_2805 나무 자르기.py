# https://velog.io/@guswns3371/%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%EB%A7%A4%EA%B0%9C-%EB%B3%80%EC%88%98-%ED%83%90%EC%83%89

# 매개 변수 탐색?

# 정렬이 안되어있는데 이걸 이분탐색으로 부를 수 있나..

# 반드시 정렬되어 있을 때 쓴다는 아니고

# 데이터의 크기가 크고 정렬된 상태에서 원하는 항목을 찾을 때

# 주로 쓴다고 함. (근데 대부분의 설명에는 정렬되어 있어야 한다고 되어있음..)

# 우선 문제가 잘 이해가 안된다..

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tree_heights = list(map(int, input().split()))

h = 0

left, right = 0, max(tree_heights)

while left <= right:
    mid = (left + right) // 2

    # 1. 나무 잘라서 잘린 나무들 합이랑 중간값 비교하기
    tree_sum = 0
    for tree in tree_heights:
        if tree > mid:
            tree_sum += tree - mid

    # 2. m과 비교
    if tree_sum >= m:
        ans = max(mid, h)

        # h를 늘려서 탐색한다. (최적해 찾아가기)
        left = mid + 1
    else:
        # h를 줄여서 탐색한다. (나무가 모자라니까)
        right = mid - 1

# 정답 출력
print(h)





