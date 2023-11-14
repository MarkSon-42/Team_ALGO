import sys
my_input = sys.stdin.readline


def back_tracking(cnt, idx):
    if cnt == l:
        vo, co = 0, 0  # vo: 모음, co: 자음

        for i in range(l):
            if answer[i] in vowel:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(cnt+1, i+1)
        answer.pop()


l, c = map(int, my_input().split())
words = sorted(list(map(str, my_input().split())))
vowel = ['a', 'e', 'i', 'o', 'u']
answer = []
back_tracking(0, 0)
