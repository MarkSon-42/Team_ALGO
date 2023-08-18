'''
문제 : 행렬 테두리 회전하기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77485
'''
import copy
def solution(rows, columns, queries):
    answer = []
    
    # grid 만들어주기
    grid = []
    for i in range(rows):
        temp = []
        for j in range(1, columns+1):
            temp.append(columns*i + j)
        grid.append(temp)
        
    # 탐색 시작
    for q in queries:
        r1, c1, r2, c2 = q[0], q[1], q[2], q[3]
        
        # 회전할 때마다 비교해줘야됨
        smallest = 101

        # 회전에 필요한 값을 저장해줄 temp 행렬 선언
        temp = copy.deepcopy(grid)
        # 범위 지정
        for r in range(r1-1, r2):
            for c in range(c1-1, c2):
                # 테두리가 아닌 애들을 제외하려면, 조건은 다음과 같다.
                # 특정 좌표가 r1-1보다 크고, r2-1보다 작고, c1-1보다 크고, c2-1보다 작아야 한다.
                if (r > r1-1 and r < r2-1) and (c > c1-1 and c < c2-1):
                    continue
                # 상하좌우, 어디로 밀어야 할 지 정해야 한다. 기준은 다음과 같이 잡자.
                # 위로 미는 경우
                if (r > r1-1 and r <= r2-1) and (c == c1-1):
                    grid[r-1][c] = temp[r][c]
                    smallest = min(smallest, temp[r][c])
                # 아래로 미는 경우
                if (r >= r1-1 and r < r2-1) and (c == c2-1):
                    grid[r+1][c] = temp[r][c]
                    smallest = min(smallest, temp[r][c])
                # 왼쪽으로 미는 경우
                elif (r == r2-1) and (c > c1-1 and c <= c2-1):
                    grid[r][c-1] = temp[r][c]
                    smallest = min(smallest, temp[r][c])
                # 오른쪽으로 미는 경우
                elif (r == r1-1) and (c >= c1-1 and c < c2-1):
                    grid[r][c+1] = temp[r][c]
                    smallest = min(smallest, temp[r][c])
        answer.append(smallest)
    return answer
print(solution(6, 6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))