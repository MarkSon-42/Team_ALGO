# 문제의 분류가 너무 힌트... 배낭 문제처럼 유형이 어느정도 보이니 그리디를 떠올리면 됨.
# 거스름돈 문제도 마찬가지..

def solution(people, limit):
    people.sort()  # 사람들의 무게를 오름차순으로 정렬
    count = 0  # 구명보트의 수를 카운트하기 위한 변수
    start = 0  # 가장 가벼운 사람의 인덱스
    end = len(people) - 1  # 가장 무거운 사람의 인덱스

    while start <= end:
        if people[start] + people[end] <= limit:  # 가장 가벼운 사람과 무거운 사람이 함께 탈 수 있는 경우
            start += 1  # 가장 가벼운 사람과 무거운 사람이 함께 탑승
        end -= 1  # 무거운 사람은 항상 탑승
        count += 1  # 구명보트 수 증가

    return count
