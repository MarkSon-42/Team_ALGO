'''
문제 : H_Index
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''
def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)

    # h번 이상 인용된 논문이 현재 인덱스보다 많다면 조건에 부합한다. 최대값만 구하면 되니까 그 아래는 볼 필요가 없음.
    # 5 4 3 3 1 을 예시로 보면 i = 3, citations[i] = 3 으로 적합
    for i in range(n):
        if i >= citations[i]:
            answer = i
            break
    # 모든 인용횟수가 같다면 길이가 답이다
    return n