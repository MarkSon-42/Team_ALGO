'''
문제 : 행렬의 곱셈
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12949
'''
def solution(arr1, arr2):
    answer = []
    
    # arr1의 행, 열, arr2의 행, 열
    lc, lr, rc, rr = len(arr1), len(arr1[0]), len(arr2), len(arr2[0])
    # 결과는 lc x rr 의 크기를 가진 행렬
    
    for i in range(lc):
        tempArr = []
        temp = 0
        for j in range(lr):
            # arr1의 [i][j]
            Lelement = arr1[i][j]
            for k in range(rr):
                for j in range(rc):
                    Relement = arr2[j][k]
                    
        answer.append(temp)
            
    
    
    return answer