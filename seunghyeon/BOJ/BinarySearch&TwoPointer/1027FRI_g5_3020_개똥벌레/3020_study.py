from sys import stdin
input = stdin.readline
n, h = map(int, input().split())
mite, tite = [], [] # 석순, 종유석

def binarySearch_UpperBound(start, end, arr, target):
    while start < end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

for i in range(n//2):   # 입력 횟수 절반으로 줄임
    mite.append(int(input())) # 석순
    tite.append(h-int(input())) # 종유석    # [6, 4, 2]

mite.sort()   # 석순 오름차순 정렬
tite.sort()   # 종유석 오름차순 정렬

min_num, result = n, 0

for i in range(1, h+1):
    r1 = n//2 - binarySearch_UpperBound(0, n//2, mite, i-1)     # 닿은 면 체크
    r2 = binarySearch_UpperBound(0, n//2, tite, i-1)   # 닿지 않은 면 체크
    total = r1 + r2 # (총 닿은 면 개수)
    if min_num == total:
        result += 1
    elif min_num > total:
        min_num = total
        result = 1

print(min_num, result)
