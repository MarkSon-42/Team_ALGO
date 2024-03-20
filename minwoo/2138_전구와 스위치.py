n = int(input())
bulb = list(map(int, input()))
to = list(map(int, input()))



def switch_bulb(a, b):
    l = a[:]
    cnt = 0

    for i in range(1, n):
        if l[i - 1] == b[i - 1]:
            continue
        cnt += 1

        for j in range(i - 1, i + 2):
            if j < n:
                l[j] = 1 - l[j]

    return cnt if l == b else 1e9

answer = switch_bulb(bulb, to)

bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
answer = min(answer, switch_bulb(bulb, to) + 1)
print(answer if answer != 1e9 else -1)

# 좀 이해가 안가요..