# 기초 수학 지식의 부재

# 30의 배수 조건은

# 각 자리수를 다 더했을 때, 3으로 나누어 떨어지고 일의 자리수가 0이면 된다

n = list(input())
n.sort(reverse=True)

_sum = 0

for num in n:
    _sum += int(num)

if _sum % 3 == 0 and '0' in n:
    print(''.join(n))
else:
    print(-1)


# 이 문제는 그런가보다.. 하고 넘어가자