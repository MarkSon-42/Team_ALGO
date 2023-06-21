def solution(n, arr1, arr2):
    answer = []
    
    grid1 = []
    grid2 = []
    
    # 1. 2진법으로 바꾼 수의 길이가 n보다 작을 경우, n-(2진법수 길이) 만큼 0 을 앞에 붙여준다.
    for i in arr1:
        temp = format(i, 'b')
        if len(str(temp)) < n:
            temp = str(temp).zfill(n)
            grid1.append(temp)
        else:
            grid1.append(str(temp))
    
    for i in arr2:
        temp = format(i, 'b')
        if len(str(temp)) < n:
            temp = str(temp).zfill(n)
            grid2.append(temp)
        else:
            grid2.append(str(temp))
    
    
    # 2. 이걸 각각 grid1, grid2로 갱신해준 다음, grid1과 grid2를 돌면서 새로운 지도를 만들어준다. 이 때, 0은 공백, 1은 #으로 만들어준다.
    for i in range(n):
        temp = ''
        for j in range(n):
            # 둘 중 하나라도 1이면
            if int(grid1[i][j]) + int(grid2[i][j]) > 0:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    
    return answer

solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28])