import sys
t = int(input())
for _ in range(t):
    fashion = {}
    m = int(input())
    for _ in range(m):
        name = sys.stdin.readline().split()
        if name[1] in fashion:
            fashion[name[1]] += 1
        else:
            fashion[name[1]] = 1
    answer = 1
    for elem in fashion.values():
        answer *= (elem + 1)
    print(answer - 1)