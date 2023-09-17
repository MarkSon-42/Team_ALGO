import sys
input = sys.stdin.readline

coins = [500, 100, 50, 10, 5, 1]

change = 1000 - int(input())
cnt = 0

for coin in coins:
    while change >= coin:
            change -= coin
            cnt += 1

print(cnt)

