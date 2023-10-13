# heapq를 사용하는게 더 효율적일까, deque를 사용하는게 더 효율적일까
# 각 개념의 특징과 대표 활용에 대해 익숙해지기
# solved라는 defaultdict를 만들어 사용하는 이유
	# heapq를 통해 만든 min heap, max_heap은 중간 원소 삭제가 불가능하기 때문
import heapq as hq
from collections import defaultdict
import sys

my_input = sys.stdin.readline


def execute_inst(prob_lst, inst_lst):
	min_heap, max_heap = [], []
	solved = defaultdict(int)

	# 최대힙, 최소힙 초기화
	for prob, lev in prob_lst:
		hq.heappush(min_heap, (lev, prob))
		hq.heappush(max_heap, (-lev, -prob))

	# 명령어 수행
	for inst in inst_lst:
		inst = inst.split()
		# [3] 문제 번호 출력
		if inst[0] == "recommend":
			# 가장 어려운 문제 출력 (여러 개라면 가장 큰 번호)
			if inst[1] == "1":
				while solved[abs(max_heap[0][1])] != 0:
					solved[abs(max_heap[0][1])] -= 1
					hq.heappop(max_heap)
				print(-max_heap[0][1])
			# 가장 쉬운 문제 출력 (여러 개라면 가장 작은 번호)
			else:
				while solved[min_heap[0][1]] != 0:
					solved[min_heap[0][1]] -= 1
					hq.heappop(min_heap)
				print(min_heap[0][1])
		# [4] 문제 추가
		elif inst[0] == "add":
			prob, lev = int(inst[1]), int(inst[2])
			hq.heappush(min_heap, (lev, prob))
			hq.heappush(max_heap, (-lev, -prob))
		# [5] 문제 제거
		elif inst[0] == "solved":
			solved[int(inst[1])] += 1ㄷ


N = int(my_input())
problems = [list(map(int, my_input().split())) for _ in range(N)]
M = int(my_input())
instructions = [my_input().strip() for _ in range(M)]

execute_inst(problems, instructions)


# additional
	# https://velog.io/@becooq81/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-BBST
	# https://blog.naver.com/PostView.naver?blogId=jinhan814&logNo=222421203400
