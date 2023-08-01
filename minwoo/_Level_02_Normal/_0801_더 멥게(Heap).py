import heapq

def solution(scoville, K):
    cnt = 0
    # heapify() :
    heapq.heapify(scoville)

    while scoville[0] < K:
        spicy = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, spicy)
        cnt += 1
        if len(scoville) < 2 and scoville[0] < K:
            return -1
    return cnt

# 문제에 있는걸 그대로..
# lv2인 이유는 heap자료구조를 사용해서
# python이라면 lv 0~1 로 내려가도 될듯