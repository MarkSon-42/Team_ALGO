def calculate(s):
    stack1 = []
    stack2 = []
    stack3 = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack1.append(i)
        elif s[i] == '[':
            stack2.append(i)
        elif s[i] == '{':
            stack3.append(i)
        else:
            if stack1 == [] and stack2 == [] and stack3 == []:
                return 0
            else:
                if s[i] == ')':
                    if stack1:
                        stack1.pop()
                    else:
                        return 0
                elif s[i] == ']':
                    if stack2:
                        stack2.pop()
                    else:
                        return 0
                elif s[i] == '}':
                    if stack3:
                        stack3.pop()
                    else:
                        return 0
    
    if stack1 or stack2 or stack3:
        return 0
    else:
        return 1

def solution(s):
    count = 0
    
    for j in range(len(s)):
        tmp_s = s[0]
        for i in range(len(s)):
            s = list(s)
            if i == len(s) - 1:
                s[i] = tmp_s
            else:
                s[i] = s[i + 1]
        s = ''.join(s)
        count += calculate(s)
    return count
