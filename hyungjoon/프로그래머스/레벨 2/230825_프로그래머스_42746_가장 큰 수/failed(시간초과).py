'''
문제 : 쿼드 압축 후 세기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/68936
'''
def solution(arr):
    answer = [0, 0]
    n = len(arr)
    # 분할정복 인거같은데... 몰..루
    def comp(x, y, n):
        init = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != init:
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y+nn, nn)
                    comp(x+nn, y, nn)
                    comp(x+nn, y+nn, nn)
                    return
        answer[init] += 1
    
    comp(0, 0, n)
    return answer
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))