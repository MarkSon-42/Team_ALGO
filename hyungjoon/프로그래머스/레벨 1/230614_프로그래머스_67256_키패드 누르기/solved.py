'''
문제 : 키패드 누르기
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/67256
'''

def solution(numbers, hand):
    answer = ''
    
    # 1. 숫자별로 keymap을 만들어준다.
    keymap = {
        '1' : [0, 0], '2' : [0, 1], '3' : [0, 2],
        '4' : [1, 0], '5' : [1, 1], '6' : [1, 2],
        '7' : [2, 0], '8' : [2, 1], '9' : [2, 2],
        '*' : [3, 0], '0' : [3, 1], '#' : [3, 2]
    }
    
    # 2. 현재 l과 r의 손의 위치를 저장한다. 각각 행/렬 로 저장된다.
    l, r = keymap['*'], keymap['#']
    
    # 3. numbers를 돌면서 왼손 오른손 중 뭘로 갈지 정해준다. 이 때 옮긴 손의 위치를 갱신해준다.
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            l = keymap[str(i)]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            r = keymap[str(i)]
        else:
            # 3-1. 2, 5, 8, 0은 가까운 손이 있는 친구로 이동해준다.
            # 현재 수의 좌표
            position = keymap[str(i)]
            # 현재 수로부터 각각 왼손 오른손의 거리
            ld = abs(position[0] - l[0]) + abs(position[1] - l[1])
            rd = abs(position[0] - r[0]) + abs(position[1] - r[1])
            
            if ld < rd:
                answer += 'L'
                l = keymap[str(i)]
            elif rd < ld:
                answer += 'R'
                r = keymap[str(i)]
            else:
                # 3-2. 거리가 같으면, 왼/오른손 잡이에 따라 이동
                if hand == 'right':
                    answer += 'R'
                    r = keymap[str(i)]
                else:
                    answer += 'L'
                    l = keymap[str(i)]
            
    return answer