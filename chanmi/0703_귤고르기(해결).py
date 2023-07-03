def solution(k, tangerine):
    size_dict = {}
    
    for item in tangerine:
        if item in size_dict:
            size_dict[item] += 1
        else:
            size_dict[item] = 1
            
    size_dict = sorted(size_dict.items(), key = lambda item : item[1], reverse=True)
    result = 0
    count = 0
    for item in size_dict:
        if result >= k:
            break
        else:
            result += item[1]
            count += 1
    # print(size_dict)
    return count