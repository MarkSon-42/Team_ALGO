# https://moondol-ai.tistory.com/395

def solution(n):
    answer = []
    arr = [[0] * n for _ in range(n)]
    dx ,dy = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                dx += 1
            if i % 3 == 1:
                dy += 1
            if i % 3 == 2:
                dx -= 1
                dy -= 1
            arr[dx][dy] = num
            num += 1
    for i in arr:
        for j in i:
            if j:
                answer.append(j)

    return answer
