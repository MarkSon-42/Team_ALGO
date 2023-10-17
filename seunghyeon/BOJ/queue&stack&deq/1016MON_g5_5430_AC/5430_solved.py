from collections import deque
import sys
my_input = sys.stdin.readline

T = int(my_input())

for _ in range(T):
    p = my_input().strip()
    n = int(my_input())
    flag = 1
    dq = deque(my_input().strip("[""]""\n").split(','))
    if n == 0:
        dq = deque()
    R = 0
    for inst in p:
        if inst == 'R':
            R += 1
        elif inst == 'D':
            if len(dq) == 0:
                print('error')
                flag = 0
                break
            else:
                if R % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()

    if flag == 1:
        if R % 2 != 0:
            dq.reverse()
        print('[' + ",".join(dq) + ']')
