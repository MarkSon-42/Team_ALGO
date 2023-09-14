import sys
from collections import Counter

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    employee_score = [[] for _ in range(N)]
    count = 1

    for j in range(N):
        document, interview = map(int, input().split())
        employee_score[j] = [document, interview]
    
    employee_docu = sorted(employee_score, key = lambda x:x[0])
    employee_inter = sorted(employee_score, key = lambda x:x[1])
 
    top_score = employee_docu[0][1]
    for i in range(1, len(employee_docu)):
        if employee_docu[i][1] < top_score:
            top_score = employee_docu[i][1]
            count += 1
    print(count)