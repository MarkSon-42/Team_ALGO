# https://ddingmin00.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2023-KAKAO-BLIND-RECRUITMENT-%ED%83%9D%EB%B0%B0-%EB%B0%B0%EB%8B%AC%EA%B3%BC-%EC%88%98%EA%B1%B0%ED%95%98%EA%B8%B0

def solution(cap, n, deliveries, pickups):
    # idea 1. deliveries와 pickups 리스트를 거꾸로 뒤집어 처리 ( 우선 끝집부터 탐색하기 위해서 )
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    # 전체 배송과 픽업에 걸린 총 시간을 저장하는 변수 초기화
    answer = 0

    # 각 날짜별 누적 배송과 픽업을 추적하는 변수 초기화
    d = 0
    p = 0

    # 첫째 날부터 마지막 날까지 각 날짜를 반복하며 처리
    for i in range(n):
        # 현재 날짜까지 누적 배송과 픽업 업데이트
        d += deliveries[i] # 먼 집부터 돌면서 배달 갱신
        p += pickups[i] #  ______ 수거 갱신

        # 현재 날짜의 배송과 픽업 처리
        while d > 0 or p > 0:
            # 음수가 될 때 까지 배달, 수거 작업
            # 차량 용량(cap)을 배송(d)과 픽업(p)에서 뺌
            d -= cap
            p -= cap
            # 현재 남은 날짜(n - i)에 2를 곱한 값을 answer에 더함
            # 이렇게 해서 한 라운드에 배송과 픽업에 걸리는 시간을 계산함
            answer += (n - i) * 2

    # 총 배송과 픽업에 걸린 총 시간을 반환
    return answer




#  설명 (gpt)

# cap: 배송 및 픽업에 사용되는 차량의 용량을 나타내는 정수입니다.
# n: 배송 및 픽업 데이터가 있는 일수를 나타내는 정수입니다.
# deliveries: 매일 이루어진 배달 수를 나타내는 정수 목록입니다.
# pickups: 매일 이루어진 픽업 수를 나타내는 정수 목록입니다.

# 라인 2: 배송 = 배송[::-1]
#
#
# 여기서 코드는 슬라이싱 기술 [::-1]을 사용하여 deliveries 목록을 뒤집습니다.
# 이 단계의 목적은 '배달' 목록의 데이터가 역순으로 정렬되도록 하는 것입니다(즉, 최신 날짜에서 가장 이른 날짜로).
#
# 라인 3: 픽업 = 픽업[::-1]
#
#
# 마찬가지로 이 코드는 슬라이싱을 사용하여 픽업 목록을 역순으로 정렬하여 역순으로 정렬합니다.
#
# 라인 4: 대답 = 0
#
#
# 'answer'라는 변수는 0 값으로 초기화됩니다. 이 변수는 배송 및 픽업에 소요된 총 시간을 나타내는 최종 결과를 저장합니다.
#
# 라인 6-7: d = 0 및 p = 0
#
#
# 두 개의 변수 d와 p는 0으로 초기화됩니다. 이러한 변수는 매일 누적 배송 및 픽업을 추적합니다.
#
# 9-11행: 일 단위 반복
#
#
# 코드는 변수 i로 표시되는 for 루프를 사용하여 매일 반복합니다.
#
# 12-13행: 누적 배송 및 픽업 계산
#
#
# 루프 내에서 코드는 현재 날짜의 배달 및 픽업 수를 각각 추가하여 d 및 p 변수를 업데이트합니다.
#
# 15-19행: 배송 및 픽업에 걸리는 시간 계산
#
#
# 이 섹션에서 코드는 while 루프를 사용하여 당일 배송 및 픽업을 처리하고 소요 시간을 계산합니다.
#
#
# 보류 중인 배송(d > 0) 또는 픽업(p > 0)이 있는 한 루프가 계속됩니다.
#
#
# 루프가 반복될 때마다 'd'와 'p'에서 용량 'cap'을 뺍니다. 이는 단일 라운드에서 차량의 용량을 사용하여 수행할 수 있는 배송 및 픽업의 양을 나타냅니다.
#
#
# 또한 이 코드는 answer 변수를 (n - i) * 2만큼 증가시킵니다. 이것이 수행되는 이유를 설명하겠습니다.
#
#
# (n - i): 데이터의 마지막 날까지 남은 일수(현재일 포함)를 나타냅니다. 배송 및 픽업에 걸리는 총 시간을 계산하고 있으므로 남은 일수를 고려하려고 합니다.
# * 2: 이 요소는 항목을 배달하고 픽업하는 데 걸리는 시간을 설명합니다. 각 라운드에는 배달과 픽업이 모두 포함되므로 남은 일수에 2를 곱하여 두 작업의 총 시간을 구합니다.
#
#
# 21행: 최종 답변 반환
#
#
# 마지막으로 이 함수는 모든 배송 및 픽업에 소요된 총 시간을 나타내는 계산된 '대답'을 반환합니다.

