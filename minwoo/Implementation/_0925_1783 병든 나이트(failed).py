# 그냥 범위내에 만족하는 brute-forth로 푸는게 맞는거 같다
# 규칙따위 안보인다

# ...????
visited = 1
n, m = tuple(map(int, input().split()))  # codetree에서 튜플로 입력받길래 한번 해봄.

chessboard = [[0 for _ in range(m)] for _ in range(n)]

# directions = {
#     1: '2up1right',
#     2: '1up2right',
#     3: '1down2right',
#     4: '2down1right'
# }

