# https://yunchan97.tistory.com/48

# 겨우 찾은 그나마 코드라도 읽을 수 있는 풀이..

# 곡괭이 수 * 5 만큼의 광석만 캘 수 있으므로, 광석의 크기가 이보다 더 클 경우 잘라준다.

# 광물을 연속해서 5개를 캐야하므로 5개씩 광물을 잘라서 새로운 배열에 저장한다.

# 광물은 주어진 순서대로, 곡괭이는 순서가 상관없으므로

# 광물을 다이아몬드, 철, 돌 순서대로 정렬한다.

# 1. 곡괭이의 수를 구한다.
def solution(picks, minerals):
    answer = 0
    sum = 0
    # 곡괭이의 수를 구한다.
    for i in picks:
        sum += i

    # 곡괭이로 캘 수 있는 광물만큼 자른다.
    num = sum * 5
    if len(minerals) > sum:
        minerals = minerals[:num]

    # 광물들을 조사한다.
    new_minerals = [[0, 0, 0] for _ in range((len(minerals) // 5 + 1))]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i // 5][0] += 1
        elif minerals[i] == 'iron':
            new_minerals[i // 5][1] += 1
        elif minerals[i] == 'stone':
            new_minerals[i // 5][2] += 1

    # 광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬해준다.
    new_minerals.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    # 정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
    for i in new_minerals:
        dia, iron, stone = i

        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5 * dia) + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25 * dia) + (5 * iron) + stone
                break

    return answer