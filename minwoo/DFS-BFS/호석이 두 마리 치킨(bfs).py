from collections import deque

num_nodes, num_edges = map(int, input().split())
graph = [[] for _ in range(num_nodes + 1)]
for _ in range(num_edges):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
chickens = [0] * 2

def main():
    best_chicken1, best_chicken2 = 0, 0
    min_total_cost = float("inf")
    for i in range(1, num_nodes + 1):
        chickens[0] = i
        for j in range(i + 1, num_nodes + 1):
            chickens[1] = j
            total_cost = calculate_total_cost()
            if min_total_cost > total_cost:
                min_total_cost = total_cost
                best_chicken1, best_chicken2 = i, j

    print(best_chicken1, best_chicken2, min_total_cost)

def calculate_total_cost():
    queue = deque()
    queue.append((chickens[0], 1))
    queue.append((chickens[1], 1))
    cost = [float("inf")] * (num_nodes + 1)
    cost[chickens[0]] = 0
    cost[chickens[1]] = 0
    while queue:
        current_node, current_cost = queue.popleft()
        for adjacent_node in graph[current_node]:
            if cost[adjacent_node] > cost[current_node] + 1:
                cost[adjacent_node] = cost[current_node] + 1
                queue.append((adjacent_node, current_cost + 1))
    total_cost = 0
    for i in range(1, num_nodes + 1):
        if cost[i] != float("inf"):
            total_cost += cost[i]
    return total_cost * 2

if __name__ == '__main__':
    main()