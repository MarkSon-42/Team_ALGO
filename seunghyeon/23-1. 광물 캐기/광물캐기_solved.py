def ftSort(minerals):
    i = 0
    counted = []
    flag = True
    while flag:
        target = []
        if i + 5 < len(minerals):
            target = minerals[i:i + 5]
        else:
            target = minerals[i:]
            flag = False
        dias, irons, stones = target.count('diamond'), target.count('iron'), target.count('stone')
        counted.append([dias, irons, stones])
        i += 5
    counted.sort(key=lambda _: (-_[0], -_[1]))

    return counted

def lowestFatigue(counted, picks):
    fatigue = 0

    for target in counted:
        if picks[0] > 0:
            picks[0] -= 1
            fatigue += sum(target) # 다이아몬드 곡괭이를 사용할 경우 무엇을 캐도 피로도가 1이므로 그냥 광물 수를 더해주면 된다
        elif picks[1] > 0:
            picks[1] -= 1
            fatigue += target[0] * 5 + target[1] + target[2]
        elif picks[2] > 0:
            picks[2] -= 1
            fatigue += target[0] * 25 + target[1] * 5 + target[2]
        else:
            break
    return fatigue

def solution(picks, minerals):
    # (곡괭이 수) x 5 < 광물 수인 경우, 광물 수를 (곡괭이 수) x 5개까지만 보존하고 나머진 버리기
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]
    # 광물을 5개 씩 묶어 나눈 뒤 각 묶음 내 다이아몬드, 철, 돌의 개수를 세서 파워가 센 것부터 내림차순 정렬
    counted = ftSort(minerals)
    
    return lowestFatigue(counted, picks)
