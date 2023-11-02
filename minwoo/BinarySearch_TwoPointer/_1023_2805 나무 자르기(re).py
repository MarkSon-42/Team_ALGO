import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

lower_bound, upper_bound = 1, 1_000_000_000

while lower_bound <= upper_bound:  # 왜 <= 인지 ???  적어도 라는 조건 떄문?
    mid = (lower_bound + upper_bound) // 2
    log_sum = 0
    for t in tree:
        if t >= mid:
            log_sum += t - mid
    if log_sum >= m:
        lower_bound = mid + 1
    else:
        upper_bound = mid - 1
print(upper_bound)

