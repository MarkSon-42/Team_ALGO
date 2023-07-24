def solution(str1, str2):
    # 두 글자씩 끊어서 저장할 리스트
    ja_str1 = []
    ja_str2 = []
    
    # 교집합과 합집합
    inter_list = []
    total_list = []
    
    # str1 글자쌍 만들기
    for i in range(len(str1) - 1):
        keyword_set = str1[i] + str1[i + 1]
    
        # 문자열로만 이루어졌을 경우
        if keyword_set.isalpha():
            keyword_set = keyword_set.lower()
            ja_str1.append(keyword_set)
    
        
    # str2 글자쌍 만들기
    for i in range(len(str2) - 1):
        keyword_set = str2[i] + str2[i + 1]
    
        # 문자열로만 이루어졌을 경우
        if keyword_set.isalpha():
            keyword_set = keyword_set.lower()
            ja_str2.append(keyword_set)
    
#     print(ja_str1)
#     print(ja_str2)
    
    # 교집합 구하기
    if len(ja_str1) > len(ja_str2):
        # 중복된 거 저장하는 리스트
        not_count = []
        
        for item in ja_str2:
            if item in ja_str1:
                if item not in not_count:
                    item_count = ja_str2.count(item)
                    item_count2 = ja_str1.count(item)
                    
                    if item_count > item_count2:
                        # 중복되어 있는 경우 일단 다 교집합에 넣어줌. 이 과정을 하는 반례 : ["ababab", "bababa", 43690]
                        for i in range(item_count2 - 1):
                            inter_list.append(item)
                        not_count.append(item)
                    inter_list.append(item)
                else:
                    continue
    else:
        not_count = []
        for item in ja_str1:
            if item in ja_str2:
                if item not in not_count:
                    item_count = ja_str1.count(item)
                    item_count2 = ja_str2.count(item)
                    
                    if item_count > item_count2:
                        # 중복되어 있는 경우 일단 다 교집합에 넣어줌. 이 과정을 하는 반례 : ["ababab", "bababa", 43690]
                        for i in range(item_count2 - 1):
                            inter_list.append(item)
                        not_count.append(item)
                    inter_list.append(item)
    
    # print(inter_list)
    # 합집합 구하기
    if len(ja_str1) > len(ja_str2):
        yes_count = []
        total_list = ja_str1
        for item in ja_str2:
            if item not in ja_str1:
                total_list.append(item)
            else:
                if item not in yes_count:
                    item_count = ja_str1.count(item)
                    item_count2 = ja_str2.count(item)
                    if item_count < item_count2:
                        yes_count.append(item)
                    for i in range(item_count2 - item_count):
                        total_list.append(item)
                else:
                    continue
                
    else:
        yes_count = []
        total_list = ja_str2
        for item in ja_str1:
            if item not in ja_str2:
                total_list.append(item)
            else:
                if item not in yes_count:
                    item_count = ja_str1.count(item)
                    item_count2 = ja_str2.count(item)
                    if item_count > item_count2:
                        yes_count.append(item)
                    for i in range(item_count - item_count2):
                        total_list.append(item)
                else:
                    continue
    
    # print(total_list)
    if len(inter_list) == 0 and len(total_list) == 0:
        result = 1 * 65536
    else:
        result = int(len(inter_list) / len(total_list) * 65536)
    return result