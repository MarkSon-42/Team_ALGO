import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

for _ in range(m):
    num_list.sort()
    num_list[0] = num_list[1] = num_list[0] + num_list[1]

print(sum(num_list))