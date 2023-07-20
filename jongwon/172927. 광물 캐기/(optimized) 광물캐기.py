# 백트래킹 추가 버젼

def dfs(picks, minerals, fatigability):
    global result

    if sum(picks) == 0 or not minerals:
        result = min(fatigability, result)
        return

    for i in range(len(picks)):
        if picks[i] >= 1:
            picks[i] -= 1
            mined = minerals[:5]
            fatigue = 0

            if i == 0:  # 다이아몬드 곡괭이 일 때
                fatigue += len(mined)
            elif i == 1:  # 철 곡괭이 일 때
                for mineral in mined:
                    if mineral == "diamond":
                        fatigue += 5
                    else:
                        fatigue += 1
            elif i == 2:  # 돌 곡괭이 일 때
                for mineral in mined:
                    if mineral == "diamond":
                        fatigue += 25
                    elif mineral == "iron":
                        fatigue += 5
                    else:
                        fatigue += 1

            if fatigability + fatigue < result: # 현재까지의 피로도(fatigability)와 현재 곡괭이로 캘 때 발생하는 피로도(fatigue)를 더한 값이 현재까지의 최소 피로도(result)보다 작은 경우에만 재귀적으로 dfs 함수를 호출
                dfs(picks, minerals[5:], fatigability + fatigue)

            picks[i] += 1


def solution(picks, minerals):
    global result
    result = 10 ** 6
    dfs(picks, minerals, 0)
    return result