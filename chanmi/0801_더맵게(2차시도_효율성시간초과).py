def solution(scoville, K):
    current_scoville = 0
    mix_count = 0
    scoville.sort(reverse = True)
    
    while scoville[-1] < K :
        if len(scoville) <= 1:
            return -1
        
        # 스코빌 지수 계산
        current_scoville = scoville[-1] + scoville[-2] * 2
        
        # 섞은 둘을 빼주고 새로 만든 걸 넣어줌
        mix_count += 1
        scoville.pop()
        scoville.pop()
        scoville.append(current_scoville)
        
        # pop을 쓰기 위해 내림차순으로 정렬
        scoville.sort(reverse = True)
        
    return mix_count