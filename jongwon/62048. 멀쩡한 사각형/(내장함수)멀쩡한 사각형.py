import math

def minus_square(w,h):
    minus = w % h
    
    if minus:
        return minus_square(h, minus)
    else:
        return h

def solution(w,h):
    all_square = w * h
    result = all_square - minus_square(w,h)
    return result