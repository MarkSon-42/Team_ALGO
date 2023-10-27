# 아이디어가 떠오르지 않아 블로그 공부 후 풀음
# DP 문제 쉬운 문제 스스로 풀며 보충하기!
# 이 문제는 전형적인 DP 문제이긴 했는데, 다만 메모리를 고려해야하는 문제였음
	# 메모리 사용량을 극한으로 낮추어야할 땐? 슬라이딩 윈도우 기법 생각해보자
	# DP에서 말하는 슬라이딩 윈도우 기법이란? memoization을 할 때 더 이상 사용하지 않는 값을 저장하지 않고 배열을 계속하여 갱신해주는 것
	# 또한 '배열까지 선언을 하지않고 하나의 변수에 기억' 방법도 기억하자
# https://velog.io/@hyuntall/%EB%B0%B1%EC%A4%80-2096%EB%B2%88-%EB%82%B4%EB%A0%A4%EA%B0%80%EA%B8%B0-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://my-coding-notes.tistory.com/318

import sys
my_input = sys.stdin.readline

n = int(my_input())
arr = list(map(int, my_input().split()))

max_lst, min_lst = arr[:], arr[:]

for _ in range(n-1):
	v1, v2, v3 = map(int, my_input().split())
	max_lst = [v1+max(max_lst[0:2]), v2+max(max_lst), v3+max(max_lst[1:])]
	min_lst = [v1+min(min_lst[0:2]), v2+min(min_lst), v3+min(min_lst[1:])]

print(max(max_lst), min(min_lst))
