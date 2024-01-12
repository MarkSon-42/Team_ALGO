def solution(keymap, targets):
    answer = [0] * len(targets)
    char_map = {}

    for s in keymap:
        for i in range(len(s)):
            key = s[i]
            char_map[key] = min(i + 1, char_map.get(key, float('inf')))

    for i in range(len(targets)):
        s = targets[i]
        for j in range(len(s)):
            key = s[j]
            if key in char_map:
                answer[i] += char_map[key]
            else:
                answer[i] = -1
                break

    return answer

solution(["ABACD", "BCEFD"], ["ABCD", "AABB"])