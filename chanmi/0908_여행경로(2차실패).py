def solution(tickets):
    dict_path = {}
    for path in tickets:
        if path[0] in dict_path:
            dict_path[path[0]].append(path[1])
        else:
            dict_path[path[0]] = [path[1]]
            
        if path[1] in dict_path:
            dict_path[path[1]].append(path[0])
        else:
            dict_path[path[1]] = [path[0]]

    for key in dict_path.keys():
        dict_path[key].sort()


    visited = [False] * len(tickets)
    # print(dict_path)
    # print(visited)
    root = []
        
    def dfs(node):
        root.append(node)
        # print("현재 root : ", root)
        for i in dict_path[node]:
            start = node
            end = i
            for j in range(len(tickets)):
                if end in tickets[j] and start in tickets[j]:
                    if not visited[j]:
                        visited[j] = True
                        test_var = 0
                        test_var = dfs(end)

                        if test_var == end:
                            visited[j] = False
                            root.pop()

        if False in visited:
            # print("다 못돌았음")
            return node
        
    dfs("ICN")
    return root
