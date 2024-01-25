def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()
        stack.append(num)

    return ''.join(stack)

# 정확도 91.7... why

# k = 1, number = 12

# k = 1, number = 21

