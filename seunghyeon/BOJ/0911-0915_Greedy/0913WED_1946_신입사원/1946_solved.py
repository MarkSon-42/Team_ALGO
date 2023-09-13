# memo: 이 문제는 문제를 읽고 바로 이해하지 못했었음

import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
    T = int(my_input().rstrip())
    for _ in range(T):
        N = int(my_input().rstrip())
        applicants = [[] for _ in range(N)] # [0]*n
        for i in range(N):
            docu, interview = map(int, my_input().split())
            applicants[i].append(docu) # 13,14번째줄: applicants[i] = [docu, interview]
            applicants[i].append(interview)
        applicants = sorted(applicants, key=lambda x: x[0])
        hired_cnt = 1
        person = applicants[0][1]
        for i in range(1, N):
            if applicants[i][1] < person:
                person = applicants[i][1]
                hired_cnt += 1

        print(hired_cnt)

# 입력받아 리스트만드는거 간단하게 한 줄로 쓰는 법: [list(map(int, input().split())) for _ in range(N)]
