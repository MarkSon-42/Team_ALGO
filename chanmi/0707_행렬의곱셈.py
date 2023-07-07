def solution(arr1, arr2):
    
    # 행렬은 (A X B) * (B X C)로 B가 일치할 때 (A X C) 사이즈의 결과가 나온다는 것에 착안
    m = len(arr1)
    n = len(arr2[0])
    l = len(arr1[0])
    
    answer = [[0 for j in range(n)] for i in range(m)]
    
    # 삼중 for문을 이용해 해결
    for i in range(m):
        for j in range(n):
            total = 0
            for k in range(l):
                total += arr1[i][k] * arr2[k][j]
            answer[i][j] = total
            
    return answer