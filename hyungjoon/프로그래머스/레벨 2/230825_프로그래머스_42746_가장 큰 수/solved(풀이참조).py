'''
문제 : 가장 큰 수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42746
'''
def solution(numbers):
    arr = [str(i) for i in numbers]
    arr.sort(key=lambda x:x*3, reverse=True)

    return str(int(''.join(arr)))


print(solution([6, 10, 2]))