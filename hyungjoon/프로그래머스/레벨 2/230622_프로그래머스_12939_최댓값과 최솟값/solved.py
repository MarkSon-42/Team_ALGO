import sys

def solution(s):
    
    minNum, maxNum = sys.maxsize, -sys.maxsize
    s = s.split()
    for i in s:
        minNum = min(minNum, int(i))
        maxNum = max(maxNum, int(i))
        
    return str(minNum) + ' ' + str(maxNum)