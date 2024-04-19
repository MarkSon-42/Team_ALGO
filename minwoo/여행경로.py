from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for start, end in sorted(tickets, reverse=True):
        routes[start].append(end)
    path = []
    def visit(airport):
        while routes[airport]:
            visit(routes[airport].pop())
        path.append(airport)
    visit('ICN')
    return path[::-1]