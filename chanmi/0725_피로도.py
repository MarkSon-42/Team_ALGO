import itertools

def solution(k, dungeons):
    # 던전 구조 : [최소 필요도, 소모 피로도]
    # k : 현재 피로도
    
    # 순열로 모든 경우의 수를 구한 후에 연산하기
    all_root = list(itertools.permutations(dungeons))
    
    # 돌 수 있는 던전 수를 저장하는 리스트
    dungeon_count_list = []
    
    for root in all_root:
        current_fatigue = k
        dungeon_count = 0
        is_root = True
        for i in range(len(root)):
            if current_fatigue < root[i][0]:
                is_root = False
                break
            else:
                current_fatigue -= root[i][1]
                dungeon_count += 1
        dungeon_count_list.append(dungeon_count)
    
    return max(dungeon_count_list)