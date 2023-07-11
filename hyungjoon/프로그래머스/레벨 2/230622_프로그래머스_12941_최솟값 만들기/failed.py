def solution(A,B):
    answer = 0
    n = len(A)
    
    # 가장 적게나오는 값의 규칙을 보면, 한쪽에선 최솟값, 한쪽에선 최댓값을 찾아 걔네끼리 계산하는게 제일 작은 값이 나옴
    # 근데 이게 무슨원리로 되는지도 모르겠고; 걍 때려맞춘듯 일단 시초남
    for i in range(n):
        aMin = min(A)
        bMax = max(B)
        answer += aMin * bMax
        del A[A.index(aMin)]
        del B[B.index(bMax)]

    return answer