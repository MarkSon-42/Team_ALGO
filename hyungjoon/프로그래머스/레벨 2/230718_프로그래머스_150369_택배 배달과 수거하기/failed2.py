def solution(cap, n, deliveries, pickups):
    answer = 0
    # 0. n = 100,000 이라 완탐은 안됨, 그리디 문제
    # 1. 일단, 한번에 멀리 나가야 동선이 최적화 되므로, 먼곳부터 탐색하도록 한다.
    # 다른거 다 필요없음. 이 집을 비우는데 얼만큼의 거리가 소모되는가? 로 계산하자.
    
    d, p = 0, 0
    
    for i in range(n-1, -1, -1):
        # 배달항목과 수거항목
        d += deliveries[i]
        p += pickups[i]
        # 2. 해당 집을 비우는 데 초점을 맞춰야 한다. 둘 중 큰 값이 기준으로 이 집을 몇번 와야하는지 정한다.
        visit = max(d, p)
        while visit > 0:
            visit -= cap
            answer += (i+1)
    
    return answer