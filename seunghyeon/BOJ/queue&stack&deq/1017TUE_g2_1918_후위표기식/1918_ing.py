# 17:40 ~

import sys
my_input = sys.stdin.readline()

input_str = list(my_input())
stack = []
res = ''
for s in input_str:
    if s.isalpha():
        res += s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)
