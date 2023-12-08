n, curr_x, curr_y = tuple(map(int, input().split()))
a = [[0] * (n + 1)]
# line 2 padding [0]

for _ in range(n):
    a.append([0] + list(map(int, input().split())))

visited = []

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n


def can_go(x, y, curr_num):
    return in_range(x, y) and a[x][y] > curr_num


# 조건에 맞춰 움직여봅니다.
# 움직였다면 true를 반환하고
# 만약 움직일 수 있는 곳이 없었다면 false를 반환합니다.
def simulate():
    global curr_x, curr_y

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인합니다.
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy

        # 갈 수 있는 곳이라면
        # 이동하고 true를 반환합니다.
        if can_go(next_x, next_y, a[curr_x][curr_y]):
            curr_x, curr_y = next_x, next_y
            return True

    return False


    # zip() :
    # for dx,dy in zip(dxs,dys):
    #     nx,ny = r+dx, c+dy
    #     if in_range(nx,ny) and grid[nx][ny] > max_number:
    #         r,c = nx,ny
    #         break



# 초기 위치에 적혀있는 값을 답에 넣어줍니다.
visited.append(a[curr_x][curr_y])
while True:
    # 조건에 맞춰 움직여봅니다.
    greater_number_exist = simulate()

    # 인접한 곳에 더 큰 숫자가 없다면 종료합니다.
    if not greater_number_exist:
        break

    # 움직이고 난 후의 위치를 답에 넣어줍니다.
    visited.append(a[curr_x][curr_y])

for num in visited:
    print(num, end=' ')