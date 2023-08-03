def solution(prices):
    pricesLen = len(prices)
    answer = [0] * len(prices)

    for i in range(pricesLen):
        for j in range(i, pricesLen-1):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                break

    return answer
