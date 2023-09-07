def solution(str1, str2):
    strings = []
    for string in [str1, str2]:
        conv = string.upper()
        convs = {}
        for i in range(1, len(conv)):
            word = conv[i - 1] + conv[i]
            if word.isalpha():
                convs[word] = convs.get(word, 0) + 1
        strings.append(convs)

    str1, str2 = strings
    interaction = []
    for s1 in str1:
        if s1 in str2:
            interaction += [s1 for _ in range(min(str[s1], str2[s1]))]
    
    union = []
    jaccard_keys = list(str1.keys()) + list(str2.keys())
    for j in set(jaccard_keys):
        union += [j for _ in range(max(str1.get(j, 0), str2.get(j, 0)))]
    
    n = len(interaction) / len(union) if len(union) != 0 else 1

    return int(n * 65536)