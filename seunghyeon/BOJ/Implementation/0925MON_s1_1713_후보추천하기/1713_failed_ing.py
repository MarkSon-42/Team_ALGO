# 제출 37%에서 런타임에러(TypeError)이 뜨는데 아직 해결 못함 + 정리되지 못한 늘어진 코드,로직이라고 생각

from collections import deque
import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	frame_num = int(my_input().rstrip())
	total_recommend = int(my_input().rstrip())
	recommends = list(map(int, my_input().split()))

	frames = deque([[0, 0] for _ in range(frame_num)])
	for r in recommends:
		not_in_frames = 0
		for f in frames:
			# 1. 이미 사진이 걸려있는 경우
			if f[0] == r:
				f[1] += 1
				not_in_frames = 1
				break
		# 2. 사진이 걸려있지 않은 경우
		if not_in_frames == 0:
			min_recommend, is_there_empty = 1001, 1
			min_recommends = []
			tmp_idx = 0
			for f in frames:
				# 2-1. 빈 프레임이 있는 경우
				if f[0] == 0 and f[1] == 0:
					f[0], f[1] = r, 1
					is_there_empty = 0
					break
				else:d
					if f[1] <= min_recommend:
						min_recommend = f[1]
						min_recommends.append([f, tmp_idx])
				tmp_idx += 1
			# 2-2. 빈 프레임이 없어 교체를 해야하는 경우
			if is_there_empty == 1:
				if len(min_recommends) == 1:
					frames[min_recommends[0][1]] = min_recommends[0]
				else:
					min_recommends = sorted(min_recommends, key=lambda x: (x[0][1], x[1]))
					del frames[min_recommends[0][1]]
					frames.append([r, 1])

	# frames = sorted(frames, key=lambda x: x[0])
	rst_lst = []
	for frame in frames:
		if frame[0] != 0:
			rst_lst.append(str(frame[0]))
	rst_lst = sorted(rst_lst)
	print(' '.join(rst_lst))
	# print(frames[0][0], frames[1][0], frames[2][0])  # 왜 이렇게하면 그냥 틀렸습니다가 뜨는가?
