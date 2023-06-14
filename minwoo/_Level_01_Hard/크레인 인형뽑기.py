# 그림 부터가 스택이다.
# n*n 배열에서 -> 충분히 큰 바구니(스택)
# 2차원 배열 요소는 인형의 종류 1 ~ 100
# moves의 요소는 board의 열의 번호임 - 어느 열에서 맨 위에 인형을 뽑는지?
# 순서대로 스택에 넣고, stack top, top-1 이 같은 숫자이면 pop을 2번하면 될 것이다.

def solution(board, moves):
    answer = 0
    bucket = []
    # moves[m]에 따라 집게가 이동하면서 pop() 하면 된다

    for m in moves:
        for i in range(len(board)):
            kakao = board[i][m - 1]
            if kakao != 0:
                bucket.append(kakao)
                board[i][m - 1] = 0
                break

        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            bucket.pop()
            bucket.pop()
            answer += 2

    return answer