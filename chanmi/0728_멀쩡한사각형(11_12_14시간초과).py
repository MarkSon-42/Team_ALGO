def solution(w,h):
    
    # 쓸 수 없는 정사각형 수
    not_use_square = 0
    before_bound = 0
    for i in range(1, w + 1):
        ratio = h * i / w
        int_ratio = 0
        if int(ratio) < ratio:
            int_ratio = int(ratio) + 1
        else:
            int_ratio = int(ratio)
            
        if i == 1 :
            # print("첫 번째 범위 : 0 ~", int_ratio)
            not_use_square += int_ratio
            before_bound = int(ratio)
        else:
            # print("다음 범위 :", before_bound, "~", int_ratio)
            tmp = int_ratio - before_bound
            not_use_square += tmp
            before_bound = int(ratio)
            
    return w * h - not_use_square