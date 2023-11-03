# 예제 1은 t = 1 일때 인가..?

# 1 : x
# 4 : n
# 9999998 : l(1)
# 1 : l(2)
# 2 : l(3)
# 9999999 : l(4)
# 문제를 잘못 이해한?

# 아.... 나노미터와 센티미터

# 10센티미터 = 1000000000나노미터

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x = int(input()) * 100_000_000  # 나노미터로 변환
    n = int(input())
    lego_peices = [int(input()) for _ in range(n)]
    lego_peices.sort()  # 시간제한 5초다 정렬 하자.
    lower_bound, upper_bound = 1, n - 1
    accurate_peices = lego_peices[0] + lego_peices[len(lego_peices) - 1]
    # 근데 이건 target값이 있는게 아니기 때문에 이분탐색이 아닌가? mid가 필요한지 의문
    while lego_peices < upper_bound:  # 레고는 반드시 2조각을 더해야 하고, 정답 여러개일시 |l(1) - l(2)|이니까 부등호만
        mid = (lower_bound + upper_bound) // 2
        if accurate_peices == mid:
            print('yes' + lego_peices)


# 아.. 거의 다 풀었는데 까비..ㅠㅜ  -> x

# while안에 try-except를 구현한 경험이 전무하다.



