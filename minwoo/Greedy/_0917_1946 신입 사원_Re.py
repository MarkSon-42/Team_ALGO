import sys

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort()  # 람다 없이도, default로 arr[i][j]에서 i를 기준으로 정렬된다.

    cnt = 1
    _max = arr[0][1] # 정렬을 이미 했기 때문에 cnt = 1로 두고, max(서류 1등의 2차면접 점수를 기준으로)를 초기화 한다.
    for i in range(1, n):
        if _max > arr[i][1]: # 2차 면접의 값들 비교
            cnt += 1  # 위 조건문이면.. 서류 혹은 면접중 하나이상은 통과이기에 += 1
            _max = arr[i][1]

    print(cnt)


