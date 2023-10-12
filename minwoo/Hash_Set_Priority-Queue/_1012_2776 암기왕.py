# set 문제인듯
# 그냥 list탐색하면 시초날게 분명 n, m ~1_000_000


t = int(input())
for _ in range(t):
    n = int(input())
    note_1st = set(input().split())
    m = int(input())
    note_2nd = set(input().split())
    for number in note_2nd:
        if number in note_2nd:
            print(1)
        else:
            print(0)
