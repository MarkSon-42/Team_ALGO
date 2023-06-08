def solution(players, callings):
    for i in range(len(callings)):
        called = 0
        if callings[i] in players:
            called = players.index(callings[i])
            # caleld = 3
            tmp = ''
            players[called] = tmp
            players[called] = players[called - 1]
            players[called - 1] = tmp

    return players

# ....?