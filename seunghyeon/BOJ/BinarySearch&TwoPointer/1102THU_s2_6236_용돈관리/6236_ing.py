import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())
daily = [int(my_input()) for _ in range(n)]
l = min(daily)
r = sum(daily)

while l <= r:
    mid = (l + r) // 2
    charge = mid
    num = 1
    for i in range(n):
        if charge < daily[i]:
            charge = mid
            num += 1
        charge -= daily[i]

    if num > m or mid < max(daily):
        l = mid + 1
    else:
        r = mid - 1
        k = mid
print(k)
