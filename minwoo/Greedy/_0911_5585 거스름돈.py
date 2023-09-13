# boj 5585 greedy
import sys
input = sys.stdin.readline
coins = [500, 100, 50, 10, 5, 1]
stuff = 1000 - int(input())
cnt = 0

for coin in coins:
    if stuff == 0:
        break

    cnt += stuff // coin
    stuff %= coin

print(cnt)