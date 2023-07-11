def solution(clothes):

    # 카테고리별 옷을 저장하기 위한 dict 변수
    cloth_dict ={}

    for item in clothes:
        ## 1. 이미 dict 변수에 해당 카테고리가 저장된 경우
        if item[1] in cloth_dict:
            # 이미 value는 리스트 형태로 저장되어 있으므로, append를 사용해 아이템 추가
            tmp_list = cloth_dict[item[1]]
            tmp_list.append(item[0])
            cloth_dict[item[1]] = tmp_list
            
        ## 2. 해당 카테고리의 아이템이 처음인 경우
        else:
            # 딕셔너리 변수의 key나 value는 immutable한 값만 가능하므로 튜플형 변수 이용
            item_tuple = (item[0], item[1])
            cloth_dict[item_tuple[1]] = item_tuple[0]
            
            # 이후 가공이 편하도록 tuple형태로 넣었던 value값을 리스트 형태로 변환해줌
            # 리스트 형태로 바꾸면 나중에 append 함수를 통해 원소값 추가가 용이하며
            # 카테고리 내부에 아이템이 몇 개 있는지 세기도 쉬움
            tmp_item = cloth_dict[item[1]]
            tmp_list = [tmp_item]
            cloth_dict[item[1]] = tmp_list
    
    # 의상을 저장하는 dict 변수의 생성이 끝나면, 의상의 조합을 세어야 함
    # 1개씩 입었을 때 나올 수 있는 수는 dict 변수의 길이와 동일
    category_len = len(cloth_dict)
    
    # 조합으로 해결하려고 했으나 실패.
    # 찾아보니 카테고리의 종류가 n개라고 할때 최종 결과값은 (n차 방정식의 계수의 합 - 1)임
    
    # n차방정식적인 접근
    total = 1
    print(cloth_dict)
    for key in cloth_dict.keys():
        print(key)
        tmp_len = len(cloth_dict[key]) + 1
        total *= tmp_len
        print(tmp_len)
    
    return total - 1