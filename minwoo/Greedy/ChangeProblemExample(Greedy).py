def greedy_change(coins, amount):
    # 동전 액면가 내림차순 정렬
    coins.sort(reverse=True)

    # 총 동전 개수와 남은 금액 추적을 위한 변수 초기화
    total_coins = 0
    remain = amount

    # 동전 액면가를 반복합니다.
    for coin in coins:
        # 현재 동전을 사용할 수 있는 횟수를 계산합니다.
        num_coins = remain // coin

        # 사용된 동전의 총 개수를 업데이트합니다.
        total_coins += num_coins

        # 남은 금액을 업데이트합니다.
        remain -= num_coins * coin

        # 남은 금액이 0이 되면, 거스름돈을 성공적으로 만들었습니다.
        if remain == 0:
            break

    # 여전히 남은 금액이 있다면, 정확한 거스름돈을 만들 수 없는 상황입니다.
    if remain > 0:
        return "거스름돈 불가능"
    else:
        return total_coins