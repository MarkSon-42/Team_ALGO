import math

def solution(w, h):
    # 대각선이 지나는 패턴은 반복됨.
    # 가로 0~2, 2~4, 4~6, 6~8에서 잘려나가는 선이 반복되는 것 확인 가능
    # 세로 0~3, 3~6, 6~9, 9~12에서 잘려나가는 선이 반복되는 것 확인 가능
    # 2 * 3일때는 4개가 사라짐
    # 4 * 6일때는 8개가 사라짐
    # 6 * 9일때는 12개가 사라짐
    # 8 * 12일때는 16개가 사라짐
    
    # 최대공약수의 갯수만큼 가로세로 패턴이 반복됨
    # 가장 최소에서 잘린 정사각형을 빼고 사각형을 합치면
    # 가로 w-1, 세로 h-1인 직사각형이 나옴
    
    gcd = math.gcd(w, h)
    tmp_w = w // gcd
    tmp_h = h // gcd

    square_number = (tmp_w - 1) * (tmp_h - 1)
    # 가장 작은 부분의 잘려나간 사각형 개수
    cut_square = tmp_w * tmp_h - square_number
    
    answer = w * h - cut_square * gcd
    return answer
