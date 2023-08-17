# 5를 반복해서 사용하는것에 초점을 맞춰서 5를 1개씩 늘려서 쓸때마다의 점화식을 구하는 것을 시도

def solution(N, number):
    d = [0] * (number+1) # 결과 받을 dp테이블 생성
    minimum = 0
    case = 0
    d[1] = 1 # 5를 한번만 사용
    d[2] = 5 # 5를 2번 사용 : 55, 5+5, 5-5, 5/5, 5*5
    # 알 수 있는 점 : 55는 5를 이어 붙인 수 이고, d[1]에서 만든 수로 사칙연산을 한 숫자들로 d[2]가 만들어진다.
    
    for i in range(3, N+1):
        # 5를 i번 사용했을 때의 나올 수 있는 경우의수 점화식
        d[i] = d[i-1] + (4*(i-1))
    
    # 4는 각 5마다 4칙연산을 해주므로 4를 곱해준다.
    # -> 이것을 풀어서 생각하면 각 수에 4칙연산을 해야한다.
        
    if minimum > 8:
        case = -1
    # 8번째 반복까지만 도출하면 반복 탈출 가능할 것같다.
    
    
    return case