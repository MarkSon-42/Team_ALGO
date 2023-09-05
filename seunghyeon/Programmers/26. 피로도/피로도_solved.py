answer = 0

def dfs(now, cnt, dungeons, chk):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if now >= dungeons[i][0] and chk[i] == 0:
            chk[i] = 1
            dfs(now - dungeons[i][1], cnt + 1, dungeons, chk)
            chk[i] = 0


def solution(k, dungeons):
    chk = [0] * len(dungeons)
    dfs(k, 0, dungeons, chk)

    return answer
