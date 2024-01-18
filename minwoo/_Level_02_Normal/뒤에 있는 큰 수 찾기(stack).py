
def solution(numbers):
    # 결과를 저장할 리스트
    result = [-1] * len(numbers)
    # 각 원소별로 이전에 저장한 뒷 큰 수를 저장할 객체
    stack = []
    for i in range(len(numbers) - 1, -1, -1):
        # 스택에서 현재 원소보다 큰 수를 찾는다
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        # 찾은 수가 있으면 결과에 저장
        if stack:
            result[i] = stack[-1]
        # 현재 원소를 스택에 저장
        stack.append(numbers[i])
    return result


solution([2, 3, 3, 5])