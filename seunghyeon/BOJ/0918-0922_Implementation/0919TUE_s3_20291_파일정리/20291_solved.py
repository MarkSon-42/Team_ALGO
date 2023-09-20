import sys

my_input = sys.stdin.readline

if __name__ == "__main__":
    N = int(my_input())
    ext_cnt = {}

    for _ in range(N):
        _, ext = my_input().rstrip().split('.')
        if ext in ext_cnt:
            ext_cnt[ext] += 1
        else:
            ext_cnt[ext] = 1  # 이렇게 하면 없던거 자동 생성됨

    sorted_ext_cnt = sorted(ext_cnt.items())
    print(sorted_ext_cnt)

    for ext, cnt in sorted_ext_cnt:
        print(ext, cnt)


# 20291_failed_timeover.py 파일에 메모해둔 문제점 해결 완료
	# 1) 파일 이름을 직접 분리하지 않고 split() 메서드를 사용하여 파일 확장자를 추출
		# 여러 개 중 필요한 것만 변수에 저장할 때, 저장하지 않을 변수명은 '_'로 설정하는거 익숙해지기!
	# 2) 중복된 확장자를 찾을 때 딕셔너리를 사용하여 확장자와 해당 개수를 효율적으로 추적


# What I studied through this code
    # 1)
        # print(type(ext_cnt.items())의 결과: <class 'dict_items'>
        # print(type(sorted(ext_cnt.items())))의 결과: <class 'list'>
        # sorted()해주는 순간 자동으로 list 됨
            # sorted(ext_cnt.items())의 결과 == sorted(list((ext_cnt.items())))의 결과
            # 따라서 굳이 dict_items을 list화 해주지말고 바로 sorted 하자

    # _, ext = my_input().rstrip().split('.')
        # 처음에 정확히 모르고 my_input().split('.')뒤로 맨 마지막에 rstrip()를 붙였다가 AttributeError: 'list' object has no attribute 'rstrip' 뜸
        # my_input().split()까지 진행되면 list가 된거임
        # 따라서 입력받은거에서 개행문자 제거하고싶으면 my_input().rstrip()로 개행문자 제거 뒤 split() 기능 수행 ㄱ