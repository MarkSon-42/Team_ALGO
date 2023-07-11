#  입력값이 2차원 배열 (HASH)
#  python dict로 풀어야 하는 듯...
#  Hint : 조건부 확률 _ 두 확률이 동시에 일어날 확률은 두 확률의 곱과 같다.
    answer = 0
    mapping = ['', '']
    # 2개 이상 착용
    for i in range(1, len(clothes) + 1):
        if i != 1:


        # 1개만 착용
        else:
            answer += len(clothes)

    return answer



# https://school.programmers.co.kr/questions/33347