def solution(n):
    cnt = 0

    for i in range(1, n + 1):
        sum_number = 0
        for j in range(i, n + 1):
            sum_number += j
            if sum_number == n:
                cnt += 1
            elif sum_number > n:
                break
    return cnt



# optimized

for i in range(1, n // 2 + 2):
    sum_number = 0
    for j in range(i, n + 1):
        sum_number += j
        if sum_number == n:
            cnt += 1
            break
        elif sum_number > n:
            break
return cnt
