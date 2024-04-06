# 스티커 회전을 어떻게 시키는지.. ㅜㅜ -> dx dy?

# 스티커 회전은 행과 열에 변화있음

# 일단 90도 회전시 행의 크기와 열의 크기가 교환됨  2 x 3 -> 3 x 2

# 코드는 보지말고 힌트 함수만.. ( 필요한 기능 정리 )

# 1. 가능한 좌표를 찾기
# 2. 놓을 수 있는지 판단하기
# 3. 회전시키기
# 4. 스티커 붙이기

# ... 쩝 ㅜㅠㅜ  https://dev-scratch.tistory.com/m/133

import sys
input = sys.stdin.readline


def rotate(s):
    s = zip(*s[::-1])
    return [list(e) for e in s]


def put(sticker):
    sr, sc = len(sticker), len(sticker[0])

    for x in range(n - sr + 1):
        for y in range(m - sc + 1):
            if compare(x, y, sr, sc, sticker):
                for sx in range(sr):
                    for sy in range(sc):
                        laptop[x + sx][y + sy] += sticker[sx][sy]
                return True

    return False


def compare(x, y, sr, sc, sticker):
    for sx in range(sr):
        for sy in range(sc):
            if laptop[x + sx][y + sy] == sticker[sx][sy] == 1:
                return False

    return True


n, m, k = map(int, input().split())

laptop = [[0] * m for _ in range(n)]
stickers = []

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)

for sticker in stickers:
    for i in range(4):
        if put(sticker):
            break
        sticker = rotate(sticker)

cnt = sum(map(sum, laptop))

print(cnt)
