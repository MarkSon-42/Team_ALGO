import sys
input = sys.stdin.readline
num = int(input())
cardDict = {}
for i in range(num):
    card_number = int(input())

    if card_number in cardDict:
        cardDict[card_number] += 1
    else:
        cardDict[card_number] = 1


sortedDict = sorted(cardDict.items(), key = lambda x: (-x[1], x[0]))
print(sortedDict[0][0])