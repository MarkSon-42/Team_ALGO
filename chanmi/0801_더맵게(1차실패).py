def solution(scoville, K):
    current_scoville = 0
    mix_count = 0
    while current_scoville < K :
        # pop을 쓰기 위해 내림차순으로 정렬
        scoville.sort(reverse = True)
        
        # 스코빌 지수 계산
        current_scoville = scoville[-1] + scoville[-2] * 2
        
        # 섞은 둘을 빼주고 새로 만든 걸 넣어줌
        mix_count += 1
        scoville.pop()
        scoville.pop()
        scoville.append(current_scoville)
        
    return mix_count