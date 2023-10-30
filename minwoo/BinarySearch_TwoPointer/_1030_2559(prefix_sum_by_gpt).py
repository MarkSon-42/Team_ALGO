import sys

input = sys.stdin.readline

n, k = map(int, input().split())
days = list(map(int, input().split()))

# 누적 합 배열 생성
prefix_sum = [0] * n
prefix_sum[0] = days[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + days[i]

max_sum = prefix_sum[k - 1]  # 초기값 설정

for right in range(k, n):
    # 누적 합을 이용하여 윈도우 내의 합 계산
    window_sum = prefix_sum[right] - prefix_sum[right - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)


# 결국 sum(*슬라이싱)이 문제였음..
# 파이썬에서 iter object에 대한 슬라이싱이 슬라이딩 윈도우 개념과 같음.
