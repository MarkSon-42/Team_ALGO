def solution(s):
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if stack:  # 스택이 비어있지 않은 경우 (위의 루프 다 돌고나서도)
        return 0
    else:
        return 1