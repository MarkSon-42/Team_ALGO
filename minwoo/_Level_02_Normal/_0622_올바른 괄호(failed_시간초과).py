# list를 다 돌기 때문에 시간초과
  

def solution(s):
    while '()' in s:
        s = s.replace('()', '')
    return len(s) == 0
