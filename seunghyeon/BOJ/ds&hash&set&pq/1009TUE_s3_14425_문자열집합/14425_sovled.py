import sys
my_input = sys.stdin.readline

N, M = map(int, my_input().split())
s_words = set([my_input() for _ in range(N)])

cnt = 0
for _ in range(M):
    word = my_input()
    if word in s_words:
        cnt += 1

print(cnt)
