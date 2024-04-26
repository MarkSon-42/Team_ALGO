# 인접한 두 어항의 값차이를 조정
def adjust(arr):
    narr = [x[:] for x in arr]      # 동시에 진행되므로 복사해서 사용!
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # 인접한 4방향, 범위내, 값이 큰 경우(i,j > ni,nj) 진행
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=i+di,j+dj
                if 0<=ni<len(arr) and 0<=nj<len(arr[ni]) and arr[i][j]>arr[ni][nj]:
                    d = (arr[i][j]-arr[ni][nj])//5
                    if d>0:
                        narr[i][j]-=d
                        narr[ni][nj]+=d
    return narr

def flatten(arr):
    narr=[]
    for j in range(len(arr[-1])):           # 가장긴 아래행(-1)길이를 기준으로
        for i in range(len(arr)-1,-1,-1):   # 역순으로 0까지 처리
            if j<len(arr[i]):               # 존재하는 범위내이면
                narr.append(arr[i][j])
    return narr

N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
while max(arr)-min(arr)>K:  # 조건을 만족할때까지 반복해서 정리
    # [1] 가장 적은 어항들에 물고기 한마리 추가
    mn = min(arr)
    for i in range(len(arr)):
        if arr[i]==mn:
            arr[i]+=1

    # [2] 공중부양 1: 2개 이상 쌓인 어항 부향 후 시계방향 90도 회전(가장 오른쪽 아래 어항 있는 동안)
    arr = [[arr[0]]]+[arr[1:]]
    while True:
        w=len(arr[-2])
        if len(arr)>len(arr[-1])-w:             # 위에 올릴 수 없는 상황이면 그만 공주부양 1
            break
        arr1 = [lst[:w] for lst in arr]
        arr2 = list(map(list,zip(*arr1[::-1]))) # 시계방향 90도 회전
        arr = arr2 + [arr[-1][w:]]

    # [3] 물고기수 조절
    narr = adjust(arr)

    # [4] 평탄화: 왼쪽바닥부터 위로 순서대로 바닥에 놓기
    arr = flatten(narr)

    # [5] 공중부양 2
    M = len(arr)//2
    narr=[arr[:M][::-1]]+[arr[M:]]
    M = M//2
    arr1 = [lst[:M] for lst in narr]        # 왼쪽절반 공중부양
    arr = [lst[::-1] for lst in arr1[::-1]] # 180도 회전
    arr += [lst[M:] for lst in narr]

    # [6] 물고기수조절 + 평탄화
    narr = adjust(arr)
    arr=flatten(narr)

    ans+=1                                  # 정리회수 +1
print(ans)