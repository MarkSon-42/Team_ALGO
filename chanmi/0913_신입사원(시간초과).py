import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    employee_score = [[] for _ in range(N)]
    for j in range(N):
        document, interview = map(int, input().split())
        employee_score[j] = [document, interview]
    
    index_list = []
    for j in range(N):
        for k in range(j + 1, N):
            if employee_score[j][0] < employee_score[k][0] and employee_score[j][1] < employee_score[k][1]:
                index_list.append(k)
            elif employee_score[j][0] > employee_score[k][0] and employee_score[j][1] > employee_score[k][1]:
                index_list.append(j)

    print(N - len(set(index_list)))