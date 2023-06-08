# 1. 시간 초과 때문에 실패 : 리스트 내에서 움직여서 시간복잡도가 o(n^2) 
def solution(players, callings):
    for i in callings:
        a = players.index(i)
        b = (a-1)
        players[b], players[a] = players[a], players[b]
        
    result = []
    for j in players:
        result.append(j)
    return result

# 2. 딕셔너리 적용
def solution(players, callings):
    players_dict = {value: key for key, value in enumerate(players)}
    rank = {value:key for key,value in players_dict.items()}
    
    for calling in callings:
        a = players_dict[calling]  
        b = a - 1
        players[b], players[a] = players[a], players[b]  
    
    return players
