# 백준에  99% 같은 문제가 있다. 번호는 기억이 안남...

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []