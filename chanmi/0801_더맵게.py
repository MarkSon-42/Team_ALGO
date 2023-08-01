import heapq

def solution(scoville, K):
    # 힙에 scoville 수치들 집어넣기
    heapq.heapify(scoville)
    
    # 섞은 횟수를 저장할 변수
    mix_count = 0
    
    while scoville[0] < K:
        # 모든 음식을 섞어도 못 만드는 경우 -1 return
        if len(scoville) <= 1:
            return -1
        
        # heappop을 이용해 가장 작은 원소 추출
        first_scoville = heapq.heappop(scoville)
        second_scoville = heapq.heappop(scoville)
        
        # 섞은 음식의 스코빌 지수 계산
        current_scoville = first_scoville + second_scoville * 2
        heapq.heappush(scoville, current_scoville)
        mix_count += 1
        
    return mix_count