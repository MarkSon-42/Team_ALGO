def solution(numbers):
    number = list(map(str, numbers))
    # 해당 문자열을 네번 반복한 뒤 길이를 계산
    # 예를 들어 3과 30이 들어올 경우, 3은 3333이 되고, 30은 30303030이 됨
    # 이후 문자열을 [:4]로 인덱싱하면 3333과 3030이 나옴.
    # 이 둘 중 큰 쪽을 우선하여 내림차순 정렬함
    number.sort(key=lambda x:(x*4)[:4], reverse=True)
    answer = "".join(number)

    # [0, 0, 0] 과 같은 답이 들어올 경우에는 '000'이 아니라 그냥 '0' 반환
    if answer[0] == "0":
      return '0'
    else:
      return answer