# 문제가 길지만 그렇다고 독해하기 어려운 케이스는 전혀 아니었다.
# 지도의 크기 n이 정말 작기 때문에 (최대 16) 시간복잡도에 대한 고민도 할 필요가 없다.
# 다만 이진수 변환을 처리하는것이 중요한데, 나의 경우 이진수 변환에 포커스가 너무 가버려서
# 이진수 변환하고 다시 문자로 변환하고 이걸 연산하겠다 이런식으로 접근했다가 실패.
# 어짜피 이진수를 1은 #으로 0은 공백으로 변환해야 함을 고려해서 지도를 생성하는 것을 한번에
# 해내는 것이 이 문제의 핵심이라 생각한다.
# 이진수 변환 -> 문자로 처리 : "하나의 함수로"

def tomap(num, n):
    result = ''  # 우선 빈 문자열을 선언해준다.
    for i in range(n):  # 맵의 크기만큼 반복문을 돈다
        if num % 2 == 1:  # 배열의 값을 2로 나누었을때 나머지가 1이라면
            result = "#" + result  # 벽이 있는것이므로 빈 문자열에 벽을 추가해준다
        else:
            result = " " + result  # 나머지가 1이 아닌경우(그러니까 나머지 0) 공백을 추가
        num //= 2  # 그리고 매 반복문마다 이렇게 요소를 다시 2로 나눈 몫으로 업데이트 해준다.
    return result


def solution(n, arr1, arr2):
    answer = ["" for i in range(n)]  # ['', '', '', '', '', '']
    map1 = []
    map2 = []

    for i in range(n):
        map1.append(tomap(arr1[i], n))
        map2.append(tomap(arr2[i], n))

        for j in range(n):
            if map1[i][j] == "#" or map2[i][j] == "#":
                answer[i] += "#"
            else:
                answer[i] += " "
    return answer


print("1" for i in range(5))