import sys

def solution(s):
    
    minNum, maxNum = sys.maxsize, -sys.maxsize
    stack = []
    # split 안쓰고 풀어보고 싶었는데 안됐당
    for i in s:
        if i == ' ':
            continue
        elif i == '-':
            stack.append(i)
        else:
            if stack:
                minNum = min(minNum, -int(i))
                maxNum = max(maxNum, -int(i))
                stack.pop()
            else:
                minNum = min(minNum, int(i))
                maxNum = max(maxNum, int(i))
                
    answer = str(minNum) + ' ' + str(maxNum)
    return answer

solution("1 2 3 4")