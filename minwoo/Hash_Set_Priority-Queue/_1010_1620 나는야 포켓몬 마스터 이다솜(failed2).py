pocketmon = {}
n, m = map(int, input().split())

for i in range(n):
    name = input()
    pocketmon[name] = str(i+1)
    pocketmon[str(i+1)] = name

for _ in range(m):
    print(pocketmon[input()])

# 이것도 시초..
# readline()이 아니라서?