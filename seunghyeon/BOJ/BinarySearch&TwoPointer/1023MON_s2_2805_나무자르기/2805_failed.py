# 11:25 ~ 12:10
# 첫 코드 완성까지 10분, but 디버깅하는데 오래걸림 (자잘한 실수 많았음 좀 더 집중해서 잘 생각하고 쓰자!)
import sys
my_input = sys.stdin.readline

# 적어도 M 미터, 절단기 높이 H
n, m = map(int, my_input().split())  # 나무의 수
trees = list(map(int, my_input().split()))
trees.sort()

trees_len = len(trees)
s, mid, e = 0, 0, trees[-1]
sums, h_sum, idx = [], 0, 0
while s <= e:
	mid = (s+e) // 2
	h_sum = 0  # h_sum을 초기화 안해줬었음
	for tree in trees:  # 처음에 조건 안걸어주고 무조건 h_sum += (tree - mid) 해서 마이너스가 나오는 경우가 생김
		if tree >= mid:
			h_sum += (tree - mid)
		else:
			continue
	if h_sum == m:
		print(mid)
		break
	elif h_sum > m:
		if idx != 0 and sums[-1][0] < m:  # 첫 코드에선 idx != 0 이 부분이 없어서 out of range 에러 남
			print(mid)
			break
		else:
			s = mid + 1
	else:
		e = mid - 1
	sums.append([h_sum, mid])
	idx += 1

# 처음 풀 때 문제에서 주어진 변수 m과 내가 중간값으로 정하려는 변수 mid를 혼동해서 다 m이라고 씀. 변수명 주의하기
# 이 코드 반례
	# 4 3
	# 1 3 3 10
	# 원하는 m보다 작았다가 커지면 그게 정답인줄알았는데, 작았다가 커졌다가 그 다음에 m과 같은 값이 나오는 경우에 대해선 해결하지 못함