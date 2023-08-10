'''
문제 : 모음 사전
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/84512
'''
def solution(word):
    dic = 'AEIOU'
    wordList = []
    
    def dfs(cnt, temp):
        if cnt == 5:
            return
        for i in range(len(dic)):
            wordList.append(temp + dic[i])
            dfs(cnt + 1, temp+dic[i])
    
    dfs(0, '')
    
    return wordList.index(word)+1