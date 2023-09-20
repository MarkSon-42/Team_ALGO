# 15:40
import sys
my_input = sys.stdin.readline

# N: 기차 수 (기차 당 20개 좌석)
# M: 명령의 수

def execute_instructions(trains_lst, instruction):
	now_train = trains_lst[instruction[1]]

	if instruction[0] == 1:
		now_train[instruction[2]] = 1
	elif instruction[0] == 2:
		now_train[instruction[2]] = 0
	elif instruction[0] == 3:
		for seat in range(19, 0, -1):
			now_train[seat] = now_train[seat-1]
		now_train[0] = 0
	else:
		for seat in range(0, 20):
			now_train[seat] = now_train[seat+1]
		now_train[19] = 0

	return trains_lst


if __name__ == "__main__":
	N, M = map(int, my_input().split())
	trains = [[0] * 20 for _ in range(N+1)]
	instructions = [list(map(int, my_input().split())) for _ in range(M)]

	for i in range(M):
		trains = execute_instructions(trains, instructions[i])
	del trains[0]
	set_trains = list(set(map(tuple, trains)))
	# 아래 부분에서 일부를 고칠게 아니라 아래 주석 전체가 별로인 것(+틀린 것) 같음
	# for idx1 in range(1, len_trains-1):
	# 	for idx2 in range(idx1+1, len_trains):  # 처음에 range(idx1+1, N)이라고 해서 IndexError: list index out of range 났었음
	# 		if trains[idx1] == trains[idx2]:
	# 			trains.remove(trains[idx2])
	print(len(set_trains))


	# 2차원 리스트 내의 요소(리스트)들 중복 잡는 법
		# 리스트 내의 요소들과 리스트를 튜플로 변환한 뒤 set()을 적용시켜주면 됨
		# 이번 문제풀이를 통해 배운 점
			# tuple은 hashable한 자료형이라서 1차원뿐만아니라 2차원 tuple에 set 함수를 적용해도 중복 제거가 됨
			# 2차원 list에 set을 적용하려고 하면 TypeError: unhashable type: 'list'가 뜸
			# 주의할 점: 2차원 리스트 내의 요소 중 '원소가 단 한 개 뿐인' 리스트는 tuple이 안돼서 string으로 바꿔야 함!

	# 3,4번 명령에 대해서 deque사용하는 로직도 짜보자