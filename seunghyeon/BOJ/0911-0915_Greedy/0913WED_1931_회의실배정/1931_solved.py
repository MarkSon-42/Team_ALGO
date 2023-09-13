import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
    N = int(my_input().rstrip())
    meetings = []
    for i in range(N):
        start, end = map(int, my_input().split())
        meetings.append([start, end])
    meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
    meetings = sorted(meetings, key=lambda x: x[1])
    # .sort(key = lambda x: (x[1], x[0]))

    cnt = 1
    end_time = meetings[0][1]
    for i in range(1, N):
        if meetings[i][0] >= end_time:
            cnt += 1
            end_time = meetings[i][1]

    print(cnt)
