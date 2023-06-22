def solution(A,B):
    answer = 0
    
    # A의 최소값과 B의 최대값을 곱한 뒤 더하는 방식
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer