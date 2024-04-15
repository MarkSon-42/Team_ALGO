# dfs인가??

# https://steadily-worked.tistory.com/807#article-2--%EB%82%9C%EC%9D%B4%EB%8F%84(solved-ac-%EC%B0%B8%EA%B3%A0)

# 솔직히 너무 어렵고,
def add(dic, arr):
    if len(arr) == 0:
        return

    if arr[0] not in dic:
        dic[arr[0]] = {}
    add(dic[arr[0]], arr[1:])


def printTree(dic, leng):
    for i in sorted(dic.keys()):
        # pr int("--" * leng + i)
        printTree(dic[i], leng + 1)


n = int(input())
a = [list(map(str, input().split())) for _ in range(n)]
dic = {}

for i in a:
    i = i[1:]
    add(dic, i)

printTree(dic, 0)