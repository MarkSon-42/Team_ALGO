import math

def solution(r1, r2):
    dotNum = 0
    for i in range(1, r2 + 1):
        h1 = 0 if i > r1 else math.sqrt(r1**2 - i**2)
        h2 = math.sqrt(r2**2 - i**2)
        dotNum += math.floor(h2) - math.ceil(h1) + 1
    
    return(dotNum * 4)
