# 입력 사항 : i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

# 수의 개수와 수 사이즈 범위를 볼때, 복잡도에 많이 신경써야 함.

# 두 수 요소를 연산해서 정답을 구하는 데 적절한 알고리즘 -> 투포인터

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for i, num in enumerate(arr):
    temp = arr[:i]+arr[i+1:]
    left = 0
    right = len(temp) - 1
    while left < right:
        if temp[left] + temp[right] > num:
            right -= 1
        elif temp[left] + temp[right] < num:
            left += 1
        else:
            result += 1
            break

print(result)