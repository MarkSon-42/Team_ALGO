# number, k의 자릿수만 보아도
# 탐색 범위를 줄이지 않으면 시간초과가 반드시 날 것이다.
# 조합, 정렬 -> 안될 가능성 99
# 작은 순서대로 k개 제거 ?
# 맨 앞 숫자 (앞자리일수록 제일 커야함)

def solution(number, k):
    number = list(number)
    result = [number.pop(0)]
    for n in number:
        if result[-1] < n:
            while result and result[-1] < n and k > 0:
                result.pop()
                k -= 1
            result.append(n)
        elif k == 0 or result[-1] >= n:
            result.append(n)

    if k:
        result = result[:-k]
    answer = ''.join(result)

    return answer