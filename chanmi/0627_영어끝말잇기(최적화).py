def solution(n, words):
    word_set = set()
    prev_word = None
    
    for idx, word in enumerate(words):
        # 중복 단어인 경우 / 이전 단어와 현재 단어의 앞뒷글자가 연결되지 않는 경우
        if word in word_set or (prev_word and prev_word[-1] != word[0]):
            
            # 여기서 idx는 for문이 몇 번 돌았는지 반복 횟수를 나타내는 값(0부터 시작함)
            # 누구 차례인지는 idx을 n으로 나눈 나머지에 1 을 더하면 알 수 있음
            # 몇 판 째 돌았는지는 idx을 n으로 나눈 값의 몫을 통해서 알 수 있음
            return [(idx % n) + 1, (idx // n) + 1]
        
        # 끝말잇기가 잘 되는 경우, 지금까지 나온 단어를 set에 저장하고 이전 단어를 prev_word에 저장함
        word_set.add(word)
        prev_word = word
    
    return [0, 0]
