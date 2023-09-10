def solution(tickets):
    dict_path = {}
    visited = {}
    for path in tickets:
        if path[0] in dict_path:
            dict_path[path[0]].append(path[1])
        else:
            dict_path[path[0]] = [path[1]]
            
        if path[1] in dict_path:
            dict_path[path[1]].append(path[0])
        else:
            dict_path[path[1]] = [path[0]]
        visited[str(path)] = False
    for key in dict_path.keys():
        dict_path[key].sort()

    # print(dict_path)
    # print(visited)
    root = []
        
    def dfs(node):
        root.append(node)
        # print(node)
        for i in dict_path[node]:
            start = node
            end = i
            first_str = "['" + str(start) + "', '" + str(i) + "']"
            second_str = "['" + str(i) + "', '" + str(start) + "']"
            # print(first_str)
            # print(second_str)
            if first_str in visited:
                if not visited[first_str]:
                    visited[first_str] = True
                    dfs(i)
            elif second_str in visited:
                if not visited[second_str]:
                    visited[second_str] = True
                    dfs(i)
        
    dfs("ICN")
    return root