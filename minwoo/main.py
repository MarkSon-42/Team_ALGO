import itertools

# 어떤 학생의 블록은 사용하지 않아도 되며 한 학생당 최대 1개의 블록만을 사용할 수 있다.
# 합이 h가 되게하는 경우의 수

# n명의 학생들과 블록 - > 데이터가 2쌍이니 리스트나 딕셔너리를?

n, m, h = map(int, input().split())
students = []
for _ in range(n):
    students += [list(map(int, input().split()))]

# i개 블록의 합으로 높이 h를 만드는 경우의 수

# permutation?

cnt = 0
tmp = ()
for i in range(m):
    for j in range(len(students[i])):
        tmp += itertools.permutations(students[j], i)
        if sum(tmp) == h:
            cnt += 1

# 딱 봐도.. 시간이 매우 걸릴것 같은 코드인데 n,m,h작아서 시도해봄

print(cnt%10007)


# 는 아니였고 dp 문제

