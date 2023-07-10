#  DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성
#  우선 LRU 캐싱부터 복습
#  코드 구현... https://eda-ai-lab.tistory.com/503을 참고해서 작성..
from collections import deque

# deque package : queue left insert, delete
def solution(cacheSize, cities):
    answer = 0
    buffer = deque()

    # (예외 처리)캐시 크기가 0인 경우에는 문제의 세번째 조건에 따라서 5를 곱한다.

    if cacheSize != 0:
        for i in cities:
            #  대소문자 구분이 없으므로 lower()로 통일해준다
            i = i.lower()
            #  캐시 히트를 처리.. 히트면 +1  아니면 +5
            if i in buffer:
                answer += 1
            else:
                answer += 5
            # LRU 정책에 따라서, 가장 오래전에 참조된.. 그러니까 가장 오래된 것을 제거
            if i in buffer:
                buffer.remove(i)
            else:
                if len(buffer) >= cacheSize:  # 버퍼가 캐시 크기를 넘겨 가득찬 경우(캐시 크기를 넘으면)
                    buffer.popleft()  #  popleft를 하게되면, 그것이 LRU에 해당하는 것을 pop.
            buffer.append(i)

    # (예외 처리)캐시 크기가 0인 경우에는 문제의 세번째 조건에 따라서 5를 곱한다.
    else:
        return len(cities) * 5

    return answer


#  다양한 풀이를 구경하고 있지만, 우선 캐싱을 코드로 구현하는 연습을 하는게 중요하고
#  자주 쓰이는 자료구조인 데크에 대해서 완벽하게 이해하고 학습하고 코드 구현 연습부터 하는게 먼저일 것이다..