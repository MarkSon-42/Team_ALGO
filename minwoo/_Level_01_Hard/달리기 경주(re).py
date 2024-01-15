# swap으로 풀면 안되는거 아는데, 그 풀이밖에 생각이 안남.

# 5 ≤ players의 길이 ≤ 50,000

# 2 ≤ callings의 길이 ≤ 1,000,000

def solution(players, callings):
    answer = players
    mapped = {player: i for i, player in enumerate(players)}

    for call in callings:
        rank = mapped[call]
        answer[rank], answer[rank - 1] = answer[rank - 1], answer[rank]
        mapped[call], mapped[answer[rank]] = rank - 1, rank

    return answer

solution(	["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])