def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    temp = 0
    print(targets)

    # 만약 현재 발사 시작 위치보다 크거나 같은 값이 나오면 발사 끝지점 temp를 갱신해준다.
    for i in targets:
        if i[0]<temp:
            continue
        else:
            answer+=1
            temp = i[1]

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))