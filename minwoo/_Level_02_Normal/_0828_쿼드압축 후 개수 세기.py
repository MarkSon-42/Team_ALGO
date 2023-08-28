# 그림에서 보듯.. 프랙탈 패턴.. 재귀 패턴

# 쿼드트리 위키피디아 링크에 들어가면 재귀라고 나와있다.

# 쿼드트리는 각 내부 노드에 정확히 4개의 자식이 있는 트리 데이터 구조
# 2차원 공간을 재귀적으로 4개의 영역으로 분할하는데 사용
def solution(arr):
    answer = [0,0]
    l = len(arr)
    def recur(arr,x,y,l):
        point = arr[x][y]
        for i in range(x,x+l):
            for j in range(y, y+l):
                if point != arr[i][j]: # 값이 다르다면, 현재 영역을 4개로 나누어 재귀 호출
                    recur(arr,x,y,l//2)
                    recur(arr,x+l//2,y,l//2)
                    recur(arr,x,y+l//2,l//2)
                    recur(arr,x+l//2,y+l//2,l//2)
                    return
        answer[point] += 1


    recur(arr,0,0,l) # ... 이렇게 호출을 해줘야 한다.

    return answer