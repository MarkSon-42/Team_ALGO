# 뭘 모르는거지?
# 모르는건 없다. 힌트도 없다.
# 그냥 문제 다시 읽고 다시 푸셈.

import sys
input = sys.stdin.readline

n = int(input())
loads_length = list(map(int, input().split()))
oil_prices = list(map(int, input().split()))
oil_price = 0

minimum_price = oil_prices[0] * loads_length[0]  # 우선 처음시작때 기름을 채워야 한다.

for i in range(1, n - 1):
    if oil_prices[i] >= oil_prices[i+1]:
        oil_price = oil_prices[i]
        minimum_price += oil_prices[i] * loads_length[i]
    else:
        pass

