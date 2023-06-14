def solution(s, skip, index):
    answer = ''

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = ''.join(sorted(list(set(alpha) - set(skip))))

    for char in s:
        idx = alpha.index(char) + index
        answer += alpha[idx % len(alpha)]
    return answer


from string import ascii_lowercase

def solution2(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}
    # 딕셔너리 컴프리헨션
    # enumerate(a_to_z)에서 반환되는 각 원소를 idx와 alpha 변수에 할당하면서 반복문을 실행
    # alpha:idx는 딕셔너리의 키-값
    #
    #
    #     위와 같은 식 (일반적인 반복문 버전)
    #
    #
    # alpha = 'abcdefghijklmnopqrstuvwxyz'
    # dic_alpha = {}
    # for i in range(len(alpha)):
    #     if alpha[i] in a_to_z:
    #         dic_alpha[alpha[i]] = i
    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result




def solution3(s, skip, index):
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in skip:
        atoz.remove(i)

    ans = ''
    for i in s:
        ans += atoz[(atoz.index(i)+index)%len(atoz)]

    return ans



def solution4(s, skip, index):
    answer = ''
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip] * 10
    # print(arr, len(arr))
    for i in s:
        answer += arr[arr.index(i) + index]
    return answer