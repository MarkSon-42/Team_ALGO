# 솔직히 너무 어려웠다.
# 난이도(상)에 해당하는 문제라고 해설에도 나와있음
# 다만 빡구현과 set 그리고
# |= 연산 배우는데 좋은 문제  or == or == or...


def solution(m, n, board):
    board = [list(x) for x in board]

    def check():
        to_remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '_':
                    to_remove |= {(i, j), (i, j+1), (i+1, j), (i+1, j+1)}
        return to_remove

    def drop():
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] == '_':
                        board[i+1][j], board[i][j] = board[i][j], '_'

    answer = 0
    while True:
        to_remove = check()
        if not to_remove:
            return answer
        answer += len(to_remove)
        for i, j in to_remove:
            board[i][j] = '_'
        drop()