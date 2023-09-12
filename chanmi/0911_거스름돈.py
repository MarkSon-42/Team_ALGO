import sys

sys.setrecursionlimit(10**6)

# 거스름돈 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
coin_list = [500, 100, 50, 10, 5, 1]
coin_count = [0] * 6

N = int(input())

change = 1000 - N
index = 0

while index != 6:
    if change - coin_list[index] >= 0:
        coin_count[index] += 1
        change -= coin_list[index]
    else:
        index += 1

print(sum(coin_count))