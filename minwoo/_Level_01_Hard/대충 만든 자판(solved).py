# 출처 : https://velog.io/@error_io/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8C%80%EC%B6%A9-%EB%A7%8C%EB%93%A0-%EC%9E%90%ED%8C%90-Lv.1-%ED%8C%8C%EC%9D%B4%EC%8D%AC

def solution(keymap, targets):
    answer = []  # 결과를 저장할 리스트인 answer를 생성
    key_dict = {}  # 문자와 열 번호를 매핑하는 딕셔너리 key_dict를 생성.

    # keymap을 탐색하여 key_dict를 채운다.
    # keymap의 각 행(row)을 i로 순회, 각 열(col)을 j로 순회.
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            char = keymap[i][j]  # 현재 위치의 문자를 char에 저장.
            if char not in key_dict:
                key_dict[char] = (j + 1)  # key