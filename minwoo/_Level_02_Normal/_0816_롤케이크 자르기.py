def solution(topping):
    answer = 0
    left = {}
    for t in topping:
        if t in left:
            left[t] += 1
        else:
            left[t] = 1

    right = {}
    for t in topping:
        if len(right) == len(left):
            answer += 1

        if t not in right:
            right[t] = 1

        left[t] -= 1

        if left[t] == 0:
            del left[t]

    return answer