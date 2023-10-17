
# pq를 이용한 방식으로도 풀어보기! (keyword: pq, sort, set)

import sys
my_input = sys.stdin.readline

# 이전 점보다 y값이 작아지는 지점에서 건물 세주기
# 단, 주의해야하는 한 가지 경우: 스카이라인 낮아지며 두 개 이상 건물이 끝나는 경우
if __name__ == "__main__":
	N = int(my_input())
	skylines = [list(map(int, my_input().split()))[1] for _ in range(N)]
	skylines.append(0)  # 0 추가하는 이유: 맨 마지막 건물까지 정상적으로 세어주려고

	stk = [0]  # stack이 비지 않게 해주는 장치 역할
	building_num = 0
	for skyline in skylines:
		height = skyline
		while stk[-1] > skyline:
			if stk[-1] != height:
				building_num += 1
				height = stk[-1]
			stk.pop()
		stk.append(skyline)

	print(building_num)







# reference to study: https://peisea0830.tistory.com/97
	# https://velog.io/@leetaekyu2077/Python-%EB%B0%B1%EC%A4%80-1863%EB%B2%88-%EC%8A%A4%EC%B9%B4%EC%9D%B4%EB%9D%BC%EC%9D%B8-%EC%89%AC%EC%9A%B4%EA%B1%B0