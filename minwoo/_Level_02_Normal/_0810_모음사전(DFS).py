def solution(word):
    global alphabet
    global dictionary

    alphabet = ["A", "E", "I", "O", "U"]
    dictionary = []

    for a in alphabet:
        DFS(a)

    return dictionary.index(word) + 1


def DFS(s):
    if len(s) > 5:
        return

    dictionary.append(s)

    for char in alphabet:
        DFS(s + char)