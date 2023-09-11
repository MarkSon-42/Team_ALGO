# DFS가 더 적합하다고 생각!

import sys
my_input = sys.stdin.readline

def find_infected_coms(start):
    visited[start] = True
    for com in graph[start]:
        if not visited[com]:
            find_infected_coms(com)


if __name__ == "__main__":
    computer_num = int(my_input().rstrip())
    edge = int(my_input().rstrip())

    graph = [[] for _ in range(computer_num+1)]
    for i in range(edge):
        x, y = map(int, my_input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (computer_num+1)

    find_infected_coms(1)
    print(sum(visited) - 1)
