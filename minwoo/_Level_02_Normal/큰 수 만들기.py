def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            k -= 1
            # 4 - > 3 2 1 0
            stack.pop()
        stack.append(num)

    while k > 0:
        stack.pop()
        k -= 1

# 반례
    # "333222111", 3
# 모든 숫자를 확인한 후에도 제거할 수 있는 숫자가 남아있는 경우
# 스택에서 숫자를 제거하는 부분을 추가해야 함.
# 주어진 숫자가 내림차순으로 정렬되어 있는 경우
# 대표적인 반례중 하나 input이 정렬되어 있을 경우!
# 같은 값이 연속적으로 있느 경우 !
    return ''.join(stack)

print(solution("333221", 5))