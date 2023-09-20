import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input())
	files = []
	for _ in range(N):
		files.append(my_input().split('.')[1])

	ext = sorted(list(set(files)))
	files_len, ext_len = len(files), len(ext)
	ext_num = [0 for _ in range(ext_len)]
	for f in files:
		if f in ext:
			ext_num[ext.index(f)] += 1

	for ext_e, ext_num_e in zip(ext, ext_num):
		print(ext_e, ext_num_e)

# What I studied through this code
	# 1) [['a'], ['b'], ['c']]와 같은 리스트의 각 원소(리스트)에 원소를 추가하고 싶을 때 꼭 .append 쓰는 방법만 있는 건 아님
		# append를 안쓰고 밑의 코드와 같이 바로 추가 가능
		#ext = [[e, 0] for e in ext]
		# 결과는 [['a', 0], ['b', 0], ['c', 0]]

# cause of failed
	# 1) 파일 확장자를 추출하는 방식
		# 문제점: files.append(my_input().split('.')[1])와 같이 파일 이름에서 직접 확장자를 추출
		# 문제가 되는 이유: 입력 파일 수 N에 대해 N번의 문자열 분리 작업이 수행되며, 이는 시간 복잡도를 높이게 됨
	# 2) 중복된 파일 확장자 찾기
		# 문제점: 파일 확장자 목록을 만들고 중복을 제거하기 위해 sorted(list(set(files)))와 같은 방법을 사용
		# 문제가 되는 이유:  중복 확장자를 찾기 위해 추가적인 정렬 및 집합 변환 작업을 수행하며, 불필요한 작업을 추가로 수행하게  됨