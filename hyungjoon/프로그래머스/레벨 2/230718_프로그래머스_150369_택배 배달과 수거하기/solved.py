'''
문제 : 택배 배달과 수거하기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150369
'''
def solution(cap, n, deliveries, pickups):
    answer = 0
    # 0. n = 100,000 이라 완탐은 안됨, 그리디 문제
    # 1. 일단, 한번에 멀리 나가야 동선이 최적화 되므로, 먼곳부터 탐색하도록 한다.
    # 배달항목과 수거항목
    d, p = 0, 0
    
    for i in range(n-1, -1, -1):
        # i번째 집을 들를 때 기존 짐과 더불어 배송/수거해야 하는 양을 계산해준다.
        d += deliveries[i]
        p += pickups[i]
        
        # 만약, 배송/수거 해야하는게 남아있다면, 어차피 나는 물류센터 갔다가 여길 다시 와야된다.
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i+1)*2
            
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))