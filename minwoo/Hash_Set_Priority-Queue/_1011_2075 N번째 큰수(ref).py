# # 종원님이 슬랙에 공유해준 풀이
# # https://naroforme.tistory.com/entry/%EB%B0%B1%EC%A4%80-2075%EB%B2%88-N%EB%B2%88%EC%A7%B8-%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# import heapq
#
# n = int(input())
# pq = []
#
# arr = list(map(int, input().split()))
#
# for num in arr:
#     heapq.heappush(arr, num)  # 처음
#
# for _ in range(n - 1):
