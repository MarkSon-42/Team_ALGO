import sys
from collections import Counter

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    employee_score = [[] for _ in range(N)]
    for j in range(N):
        document, interview = map(int, input().split())
        employee_score[j] = [document, interview]
    
    employee_docu = sorted(employee_score, key = lambda x:x[0])
    employee_inter = sorted(employee_score, key = lambda x:x[1])
 
    index_list = employee_inter[employee_docu[0][1]:] + employee_docu[employee_inter[0][0]:]
    index_list = map(tuple, index_list)
    c = Counter(index_list)

    print(N - len(c.most_common()))