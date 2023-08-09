def solution(dirs):
    visit = set()
    x = 0
    y = 0

    for d in dirs:
        if d == 'U' and y < 5:
            visit.add(((x, y), (x, y + 1)))  # 이렇게 집합 요소를 add() 연산으로 추가하는걸 몰라서 풀지 못한..
            y += 1

        if d == 'D' and y > -5:
            visit.add(((x, y - 1), (x, y)))
            y -= 1

        if d == 'R' and x < 5:
            visit.add(((x, y), (x + 1, y)))
            x += 1

        if d == 'L' and x > -5:
            visit.add(((x - 1, y), (x, y)))
            x -= 1
            
    return len(visit)