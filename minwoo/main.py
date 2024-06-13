# 애초에 코테를 올솔 목표로 접근하면 절대 안되고, 풀 수 있는걸 확실하게

# 따라서 지문 독해랑 손코딩에 시간 충분하게 써도 된다.

# 이번 달까지 선물을 주고받은 기록을 바탕으로
# 다음 달에 누가 선물을 많이 받을지 예측

# 장황한 지문 -> 사실상 문서 독해력을 테스트하려는 의도가 담김

# 필요한 부분만 찾아서 구현하는게 중요

# 구현문제에서 조합은 너무... 너무 중요하다

# gift에 대한 계산 끝내놓기

# map구조를 가진 자료형을 사용하여 선물의 주고 받음을 미리 기록해야

# 그래야 나중에 조합을 구할 떄, 선물 준 횟수, 받은 횟수, 선물 지수를 바로 계산할 수 있음

# 누가 많이 받았는지는 중요하지 않다고 한다. 그냥 높은 수가 답이므로, 이를 리턴

def solution(friends, gifts):
    answer = 0

    gift_map = {}
    giver_map = {}
    receiver_map = {}
    answer_map = {}

    # map에 friends 등록하기

    # friends = ["muzi", "ryan", "frodo", "neo"]
    for f1 in friends:
        inner_gift_map = {}
        for f2 in friends:
            if f1 == f2:
                continue  # 자기 자신은 스킵한다
            inner_gift_map[f2] = 0
        gift_map[f1] = inner_gift_map
        answer_map[f1] = 0
        giver_map[f1] = 0
        receiver_map[f1] = 0
        print(inner_gift_map)
    print(gift_map)
    print(answer_map)
    print(receiver_map)

    for gift in gifts:
        giver, receiver = gift.split()
        gift_map[giver][receiver] += 1
        giver_map[giver] += 1
        receiver_map[receiver] += 1

    print(gift_map)
    print(answer_map)
    print(receiver_map)


solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"] )




