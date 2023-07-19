# 주요 조건 (볼드체)

# k점을 여러 발 맞혀도 k점 보다 많은 점수를 가져가는 게 아니고 k점만 가져가는 것을 유의

# a = b = 0 인 경우, 즉, 라이언과 어피치 모두 k점에 단 하나의 화살도 맞히지 못한 경우는 어느 누구도 k점을 가져가지 않습니다.

# 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return -> 배열 합에서 작은 값 리턴

# 우승 방법 없으면 리턴할 배열길이는 1, 값은 -1 -> n == 1 -> return -1

# 못이기면 -1 리턴

# 라이언이 가장 큰 점수차로 우승할 과녁 배열을 구하기.

# 제한시간에 정확성 제한밖에 없으므로 완전탐색 가능.

# ! : 어피치가 중복해서 맞춘 점수판은 내주고, 못맞추거나 하나만 맞춘 것만 상회해서 맞추면 될듯

# 남은 화살 처리는 어떻게.. ?

def solution(n, info):
    answer = []
    arrow_count = n
    total_lion, total_apeach = 0, 0
    if n == 1:
        answer.append(-1)

    if n >= 2:
        for i in range(len(info)):
            if info[i] >= 2 and arrow_count != 0:
                answer.append(0)
                arrow_count -= 1

            # 남은 화살 개수를 고려해서 최대 점수차가 나게 해야 함.
            # 아래 코드는 화살 개수 제한을 처리하지 않음.
            elif info[i] == 1 and arrow_count != 0:
                answer.append(2)
                arrow_count -= 1
            elif info[i] < 1 and arrow_count != 0:
                answer.append(1)
                arrow_count -= 1


            # 화살 다 쓴 경우
            elif arrow_count == 0:
                answer.append(0)

    return answer