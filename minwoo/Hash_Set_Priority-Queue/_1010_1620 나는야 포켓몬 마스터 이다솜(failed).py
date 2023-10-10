# 도감에 수록되어 있는 포켓몬의 수 N
# 맞춰야 하는 문제의 개수 M

# 1번부터 N번까지 포켓몬

# 일부 포켓몬은 마지막 문자만 대문자..?



# in key out value
# in value out key

# 26포켓몬 주어지고 5개랄 맞춰야 함

######## IN #########
# 25
# Raichu
# 3
# Pidgey
# Kakuna

######## OUT ########
# Pikachu
# 26
# Venusaur
# 16
# 14

#
pocketmon = dict()
n, m = tuple(map(int, input().split()))


for i in range(1, n + 1):
    name = input()
    if name not in pocketmon:
        pocketmon[i] = name

# 그냥 findname이 정수형이면 value를,
# 문자열형이면 key를 리턴하면 안되나???
# 구현을 못했는데 이렇게 구현해도 value로 key탐색하는데 시간이 오래걸려서 시간초과
# 난다고 함
for i in range(m):
    findname = input()
    if findname.isalpha() and findname in pocketmon:
        print(pocketmon[i].index() + 1)
    else:
        print(pocketmon[i])
