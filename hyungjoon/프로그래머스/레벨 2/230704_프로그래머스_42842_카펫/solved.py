'''
문제 : 카펫
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''
def solution(brown, yellow):
    answer = []
    size = brown + yellow
    # 전체 사각형의 x, y 값을 구할거임
    # yellow 영역은 xy - 2(x+y) + 4 이다. 따라서 x를 for문을 해가면서, 수식에 대입했을 때 정답이면 break 해주자.
    for x in range(1, size+1):
        # 넓이가 나누어 떨어지지 않으면 패스
        if size % x != 0:
            continue
        y = size / x
        # 세로가 더 큰 케이스는 제외
        if y > x:
            continue
        if yellow == size -(2*x) -(2*y) + 4:
            answer = [x, y]
            break
            
    return answer