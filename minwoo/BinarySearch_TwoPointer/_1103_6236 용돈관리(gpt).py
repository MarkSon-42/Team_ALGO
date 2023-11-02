def check(K, N, M, expenses):
    withdraws = 0  # 인출 횟수를 추적하는 변수 초기화
    remaining = 0  # 현재 남은 금액을 추적하는 변수 초기화

    for i in range(N):  # 모든 날짜에 대해 반복
        if expenses[i] > K:  # 만약 해당 날짜의 지출이 K보다 크다면
            return False  # K로는 이 날짜를 지출할 수 없으므로 False 반환

        if remaining < expenses[i]:  # 현재 남은 금액이 이 날짜의 지출보다 작다면
            withdraws += 1  # 인출 횟수를 증가시키고
            remaining = K  # 현재 남은 금액을 K로 설정

        remaining -= expenses[i]  # 이 날짜를 지출한 만큼 현재 남은 금액을 감소

    return withdraws <= M  # 모든 날짜를 통해 인출 횟수가 M 이하인지 확인하고 결과 반환

def minimum_K(N, M, expenses):
    low, high = 1, sum(expenses)  # 이진 탐색을 위한 범위 설정 (최소 1, 최대 모든 지출 합)

    while low < high:  # 이진 탐색 반복
        mid = (low + high) // 2  # 중간값 설정

        if check(mid, N, M, expenses):  # check 함수로 중간값 K를 확인
            high = mid  # 가능한 경우, 탐색 범위의 상한을 업데이트
        else:
            low = mid + 1  # 불가능한 경우, 탐색 범위의 하한을 업데이트

    return low  # 최소 K 값을 반환

if __name__ == "__main__":
    N, M = map(int, input().split())  # 입력에서 N과 M을 읽어옴
    expenses = [int(input()) for _ in range(N)]  # N일 동안의 지출을 읽어옴

    result = minimum_K(N, M, expenses)  # minimum_K 함수 호출하여 결과 계산
    print(result)  # 결과 출력
