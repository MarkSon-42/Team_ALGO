'''
문제 : 가장 큰 수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42746
'''
from itertools import permutations as pm
def solution(numbers):
    arr = list(pm(numbers, len(numbers)))
    answer = ''.join(str(s) for s in arr[0])
    for i in arr:
        answer = max(int(''.join(str(s) for s in i)), int(answer))
    
    return str(answer)
print(solution([6, 10, 2]))