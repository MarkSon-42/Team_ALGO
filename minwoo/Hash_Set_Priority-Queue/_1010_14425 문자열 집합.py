# 이건 왜 실버 3
# -> 정답률이 높음
n, m = map(int, input().split())
string_list = []

for i in range(n):
    string_list.append(input())

cnt = 0
for i in range(m):
    if input() in string_list:
        cnt += 1

print(cnt)