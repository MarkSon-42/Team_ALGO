# 그렇게 쉬운 문제는 아닌데 시간초과 테케는 따로 없는것을 보아.. 이때문에 레벨 2인거 같음.

# 이건 이제 눈감고도 바로 함수 구현 할 줄 알아야 함.
def is_prime(n):
    if n == 1:
        return False  # 1은 소수 X
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False  # 나누어지면 역시 소수 아니니 걸러준다.
    return True

def solution(n, k):
    m = ''
    while n:
        m += str(n % k)  # 진법 변환한 수(데이터 타입은 아직 문자열), ( 아직 역순 처리는 안되있는 상태 )
        n //= k
    answer = 0

    tmp = m[::-1].split('0')  # 역순으로 뒤집어주고 0 기준으로 split() -> 0P0, 0P, P0, ..조건 맞게
    for x in tmp:
        if x:
            answer += int(is_prime(int(x)))  # 그 중에 소수인 것
            #  새로이 알게 된 것. isprime()이 불리언인데 이를 다시 int()형변환 하면 1, 0으로 나옴..
    return answer