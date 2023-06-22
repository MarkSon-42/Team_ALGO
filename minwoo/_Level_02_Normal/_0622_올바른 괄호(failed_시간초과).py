def solution(s):
    while '()' in s:
        s = s.replace('()', '')
    return len(s) == 0
