'''
문제 : 택배 배달과 수거하기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150369
'''
def solution(cap, n, deliveries, pickups):
    answer = 0
    # 0. n = 100,000 이라 완탐은 안됨, 그리디 문제
    # 1. 일단, 한번에 멀리 나가야 동선이 최적화 되므로, 먼곳부터 탐색하도록 한다.
    for i in range(n-1, -1, -1):
        # 배달항목과 수거항목
        d, p = deliveries[i], pickups[i]
        # 2. 해당 집을 비우는데 드는 resource는 d+p임. 따라서 d+p가 cap보다 크다면 두번 와야되니까 거리를 *2 해주고, 아니라면 한번만 거리에 더해준다.
        if d+p > cap:
            answer += (i+1)*2
        else:
            answer += (i+1)
    
    return answer