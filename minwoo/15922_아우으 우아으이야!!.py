n = int(input())

min_x, max_y = 9999999999, -9999999999
for i in range(n):
    x, y = map(int, input().split())
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y

print(max_y - min_x)

# 아니 구간을 두개를 잡아야지

n = int(input())

x, y = map(int, input().split())

result = 0

for i in range(n - 1):
    xx, yy = map(int, input().split())
    if xx == x:
        y = yy
    elif y >= xx and yy > y:
        y = yy
    elif y < xx:
        result += abs(x - y)
        x = xx
        y = yy

print(result + abs(y - x))
# 출처: https: // jainn.tistory.com / 41[Dogfootruler
# Kim: 티스토리]



num = int(input())

start, end = map(int, input().split())

total = 0

for i in range(num - 1):
    next_start, next_end = map(int, input().split())
    if next_start == start:
        end = next_end
    elif end >= next_start and next_end > end:
        end = next_end
    elif end < next_start:
        total += abs(start - end)
        start = next_start
        end = next_end

print(total + abs(end - start))