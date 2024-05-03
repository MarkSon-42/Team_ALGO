# https://www.youtube.com/watch?v=SEdX0CrOfCg

# 강의참고

# LIS, LCS.... 수열 시리즈

n = int(input())
arr = [0] + list(map(int, input().split())) + [0]  # 양 옆에 0 깔아줘야 루프시 비교가능.. ㄷㄷ

lis = [0 for i in range(n + 2)]

lisr = [0 for i in range(n + 2)]    

for i in range(1, n+1):
    for j in range(0, i):
        if arr[j] < arr[i]:
            lis[i] = max(lis[i], lis[j] + 1)

for i in range(n, 0, -1):
    for j in range(n+1, i, -1):
        if arr[i] > arr[j]:
            lisr[i] = max(lisr[i], lisr[j] + 1)

max_bitonic = 0

for i in range(1, n+1):
    max_bitonic = max(max_bitonic, lis[i] + lisr[i])

print(max_bitonic - 1)