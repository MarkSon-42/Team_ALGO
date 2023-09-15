# 경로상에 카메라를 설치.. 지난번 기지국 문제랑 비슷 ?
# 차량 지점이 음수부터 양수까지..
# 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주

# 가장 많이 겹치는 곳에 카메라를 설치해야.
# 들어오는 모든 값에 30,000을 더해서 전체를 양수처리할까? (?)

# https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/

# 풀이 방식 ( 그리디 문제 패턴이 조금 담겨있음 )
# 1. 진출 지점 기준으로 "오름차순 정렬"
# 2 . 최소 범위가 -30000이니 초기 카메라 위치를 -30001로 초기화 <- 이건 아이디어
# 3. routes배열을 반복하면서 카메라가 진입 지점보다 작은지 확인
# 4. 정렬을 하고 아래 조건문을 처리하면.. 그리디하게 카메라를 설치하게 된다. ( 가장 적게 설치됨. 1차원 그림을 그려보면 바로 알 수 있음. )

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치 찾음

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer