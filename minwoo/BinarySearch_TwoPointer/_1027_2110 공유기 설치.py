import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home_loc = [int(input()) for i in range(n)]
# 가정 거리가 먼 곳부터 공유기를 설치해주면서 공유기 개수를 감소시키면
# 마지막 설치할 공유기와 그 전에 공유기 설치한 위치의 거리가
# 정답이 될것

# -> x

# 이분 탐색의 개념을 알아도.. 공유기 간의 거리를 mid로 설정하고 푼다는 생각을 하기가 쉽지 않다.
# 이미 이분탐색 sudo-code를 외워버린 상태라서 공유기 사이의 거리가 mid가 아니면 뭐겠는가 싶은.. 풀어도 푼게 아닌
home_loc.sort()
lower_bound, upper_bound = 1, home_loc[n-1] - home_loc[0]
nearest_loc = 1
while lower_bound <= upper_bound:
    mid = (lower_bound + upper_bound) // 2
    count = 1
    current_loc = home_loc[0]  # 현재 공유기 설치한 위치 초기화

    for i in range(n):
        if home_loc[i] - current_loc >= mid:
            count += 1
            current_loc = home_loc[i]

    if count >= c:
        nearest_loc = mid
        lower_bound = mid + 1
    else:
        upper_bound = mid - 1

print(nearest_loc)

#