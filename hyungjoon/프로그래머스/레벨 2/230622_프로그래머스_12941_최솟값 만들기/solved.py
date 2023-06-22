def solution(A,B):
    answer = 0
    n = len(A)
    
    # 이전 아이디어 그대로 쓰고, 정렬해서 해주면 logN 됨
    for a, b in zip(sorted(A), sorted(B, reverse=True)):
        answer += a * b

    return answer