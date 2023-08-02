'''
문제 : 땅따먹기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12913
'''
def solution(land):
    answer = 0
    n = len(land)
    
    for i in range(n):
        sums = 0
        dfs(land, i, sums, 0)
        # 1. dfs로 풀어보자, 인덱스 정보를 넘겨줘서, 다음에 만나는 행이 이전 행과 동일하다면 패스
        def dfs(land, idx, sums, depth):
            for j in range(4):
                if idx == j:
                    continue
                sums += land[i][j]
            
    return answer
# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]], 16))

arr = [1,2,3,4,5]
print(arr[5:])