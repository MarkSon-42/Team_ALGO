# 좋아하는 학생들을 번호로 변환하여 저장
like_map = {}
n = int(input())
grid = [[0] * n for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
students = []

for _ in range(n * n):
    inputs = input().split()
    student = int(inputs[0])
    students.append(student)
    like = list(map(int, inputs[1:]))
    like_map[student] = like

# 학생을 배정할 때 숫자로 처리
grid[0][0] = students[0]
for i in range(1, n * n):
    stu = students[i]
    able = []
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                like, blank = 0, 0
                for k in range(4):
                    nr, nc = r + dx[k], c + dy[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] in like_map[stu]:
                            like += 1
                        elif grid[nr][nc] == 0:
                            blank += 1
                able.append([like, blank, r, c])
    able.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    grid[able[0][2]][able[0][3]] = stu

# 학생의 만족도 계산
satisfaction = 0
for r in range(n):
    for c in range(n):
        like_count = 0
        for k in range(4):
            nr, nc = r + dx[k], c + dy[k]
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] in like_map[grid[r][c]]:
                    like_count += 1
        if like_count == 0:
            satisfaction += 0
        elif like_count == 1:
            satisfaction += 1
        elif like_count == 2:
            satisfaction += 10
        elif like_count == 3:
            satisfaction += 100
        elif like_count == 4:
            satisfaction += 1000

print(satisfaction)
