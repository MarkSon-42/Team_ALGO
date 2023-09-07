# 다른 사람의 풀이를 보고 공부한 것
# 스터디 끝나고 스스로 다시 생각해서 짜볼 것
# 비트 연산자에 대해 확실히 알아볼 것

def solution(n, info):
    answer = [0 for _ in range(11)]
    tmp = [0 for _ in range(11)] # 라이언이 쏜 화살 정보 저장하기 위한 배열
    maxDiff = 0 # 가장 큰 값 업데이트 해서 저장할 변수

    for subset in range(1, 1 << 10):
        ryan = 0
        appeach = 0
        cnt = 0 # 라이언이 쓴 화살 개수 세기

        for i in range(10):
						# 라이언이 그 점수에서 이기는 경우
            if subset & (1 << i):
                ryan += 10 - i # 얻어야 할 점수
                tmp[i] = info[i] + 1 # 어피치보다 하나 더 쏘면 됨
                cnt += tmp[i] # 쏜 화살 개수 누적
						# 라이언이 그 점수에서 지는 경우
            else:
                tmp[i] = 0 # 화살을 쏘지 않음
                if info[i]: # 어피치가 점수 얻는 경우
                    appeach += 10 - i
        
        if cnt > n: continue # 사용 불가 부분집합 버리기

        tmp[10] = n - cnt # 0점에 쏠 화살의 개수

        if ryan - appeach == maxDiff: # 가장 큰 점수차가 여러 경우일 경우
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    maxDiff = ryan - appeach
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break
        elif (ryan - appeach) > maxDiff:
            maxDiff = ryan - appeach
            answer = tmp[:] # 현재 화살 정보

    if maxDiff == 0: # 라이언이 못이기는 경우
        answer = [-1]

    return answer
