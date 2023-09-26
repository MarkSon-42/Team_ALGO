# 코트에 나온 문제랑 거의 같음
# 안쪽 배열들도 회전해야 함


# https://door-of-tabris.tistory.com/entry/%EB%B0%B1%EC%A4%80-16926%EB%B2%88-%EB%B0%B0%EC%97%B4%EB%8F%8C%EB%A6%AC%EA%B8%B01python
n, m, rotation = tuple(map(int, input().split()))

com = [list(map(int,input().split()))for _ in range(n)]

# rotation만큼 회전하기

for k in range(rotation):
    inner=min(n,m)//2
    for j in range(inner):
        x,y=j,j
        pre=com[x][y]

        #좌

        for i in range(x+1,n-j):

            tmp=com[i][j]
            com[i][j]=pre
            pre=tmp

        #하

        for i in range(y+1,m-j):

            tmp=com[n-1-j][i]
            com[n-1-j][i]=pre
            pre=tmp

        #우

        for i in range(n-j-2,j-1,-1):

            tmp=com[i][m-1-j]
            com[i][m-1-j]=pre
            pre=tmp
        #상

        for i in range(m-2-j,j-1,-1):

            tmp=com[j][i]
            com[j][i]=pre
            pre=tmp


for i in range(n):
    for j in range(m):
        print(com[i][j], end=' ')
    print()
