# 8 * 8크기
#    A B C D E F G H
#  8
#  7
#  6
#  5
#  4
#  3
#  2
#  1

# 알파벳때문에 아스키처리하는게 너무 귀찮음.
# 체감상 실버1, 실3은 절대 아닌.
# 아스키 처리, 좌표도 거꾸로다 주의..
# 그리고 돌 위치도 고려해야한다. 돌이 범위 넘어서도 안됨.
# 좌표와 방향

# A -> 1
# ord(A) + 1

# dict { 'R' : (0, 1),
#        'L' : (1, -1),
#       }
import sys
input = sys.stdin.readline

def toAB(i,j):
    return chr((j-1)+ord('A'))+str(i)
def toPos(st):
    return int(st[1]), ord(st[0])-ord('A')+1



move = {
    'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
    'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, - 1)
}

king, stone, n = input().split()
n = int(n)

# 킹, 돌 좌표 변환 _ 변환 함수 2개
ki, kj = toPos(king)
si, sj = toPos(stone)

for _ in range(n):
    di, dj = move[input()]
    ni, nj = ki + di, kj + dj
    if 1 <= ni <= 8 and 1 <= nj <= 8:  # 범위 내 쳌
        if (ni, nj) == (si, sj):  # 갈 자리에 돌 있는지 체크
            ei, ej = si+di, sj+dj  # 돌의 이동할 위치
            if 1 <= ei <= 8 and 1 <= ej <= 8:
                si, sj = ei, ej
                ci, cj = ni, nj
        else:
            ci, cj = ni, nj



print(toAB(ci,cj), toAB(si,sj), sep='\n')