def solution(name):
    # 전부 A로만 이루어진 경우
    if set(name) == {'A'}:
        return 0

    # 아스키 코드
    # 'A' = 65
    # 'Z' = 90

    # 글자의 최대 상하움직임 수는 13 * len(name)
    # 좌우 움직임의 수는 20 + @이기 때문에
    # 100 등의 숫자를 주는 것보다 float('inf')로 무한대 표현을 하는 것이
    # 나중에 min 값을 계산하기 편할 수 있다.
    answer = float('inf')

    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i] # 왼쪽먼저 i칸 갔다가 + 해당 위치를 기준점으로 삼아 오른쪽으로 이동하며 글자 저장
        print("lr =", l_r)
        r_l = name[i: :-1] + name[i+1:][::-1] # 오른쪽으로 먼저 i칸 갔다가 + 해당 위치를 기준점으로 삼아 왼쪽으로 이동하며 글자 저장
        print("rl =", r_l)

        """ 예시) "JEROEN"의 경우

        i = 0 일때는 (기준점 인덱스 = 0)
        l_r = "JEROEN", r_l = "JNEORE"가 저장된다.

        i = 1 일때는 (기준점 인덱스 = 1)
        l_r = "NJEROE", r_l = "EJNEOR"가 저장된다.

        i = 2 일때는 (기준점 인덱스 = 2)
        l_r = "ENJERO", r_l = "REJNEO"가 저장된다.

        """

        for n in [l_r,r_l]:
            # 끝에 A들은 셀 필요 없으므로 자르기
            while n and n[-1] == 'A':
                n = n[:-1]

            # 글자의 이동 횟수를 count 리스트 변수에 저장해주기
            count = []
            for letter in n:
              count.append(min(ord(letter) - 65, 91 - ord(letter)))

            # 모든 글자를 다 돌아서 count가 완성되었을 때, 기존의 값과 한 번 꺾어서 i + len(count) - 1번의 움직임을 하여 읽는 방식 중
            # 더 적은 움직임의 수를 갖는 값을 answer에 저장
            answer = min(answer, i + (len(count) - 1) + sum(count))


    return answer

solution("JEROEN")