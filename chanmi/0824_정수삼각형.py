def solution(triangle):
    # 누적합 이용해서 가장 큰 값 찾기
    # 동적 프로그래밍
    
    """
         0
        0 1
       0 1 2
      0 1 2 3
    """
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][0]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][-1]
            else:
                triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j - 1], triangle[i][j] + triangle[i - 1][j])
    return max(triangle[-1])