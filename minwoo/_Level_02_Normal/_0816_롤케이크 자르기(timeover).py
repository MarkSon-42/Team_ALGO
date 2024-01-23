#  토핑의 개수에 상관없이 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 롤케이크가 나누어진 것

# 1 2 1 3 1 4 1 2

# 일단 잘라보고, set()으로 중복을 제거해서 종류를 카운트 하나?

# 공평하게 자르는 방법 가짓수 리턴.

# 1 1 1 1 1

# but.. topping length 1_000_000

# set()의 시간복잡도가 있을 터

def solution(topping):
    answer = 0
    left_cake = set()
    right_cake = set()

    for i in range(1, len(topping) - 1):
        left_cake = len(set(topping[:i]))
        right_cake = len(set(topping[i:]))
        if left_cake == right_cake:
            answer += 1
    return answer

# 이건 무조건 시초야..ㅇㅇ