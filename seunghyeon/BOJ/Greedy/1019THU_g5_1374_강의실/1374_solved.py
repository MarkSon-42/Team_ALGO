import heapq as hq
import sys
my_input = sys.stdin.readline

n = int(my_input())
lessons = [list(map(int, my_input().split())) for _ in range(n)]
lessons.sort(key=lambda x: x[1])

h = []
cnt = 0
for lesson in lessons:
	while h and lesson[1] >= h[0]:
		# h 안에서 lesson[1]보다 작거나 같으면 몇 개고 다 빼버리는게 잘 이해가 안 됐는데,
		# 어짜피 cnt는 한 번 올라가면 다시 - 되는 일은 없어서 h에서 여러 개 삭제되어도 무관
		hq.heappop(h)
	hq.heappush(h, lesson[2])
	cnt = max(cnt, len(h))  #

print(cnt)


# 입력받은 여러개의 요소(리스트 같이 여러가지 값을 담고있는 경우)를 순회하면서 처리할 때
# 무조건 전체를 그대로 사용할 필요는 없다
# 잘라서 필요한 부분만 저장하기도하고 쓰기도 하고 ..그러자..좀 더 유연해지기!