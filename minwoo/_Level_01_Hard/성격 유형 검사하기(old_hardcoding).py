def solution(survey, choices):
    help = [0, 0, 0, 0]

    for i in range(len(survey)):
        if survey[i][0] == "R":
            help[0] += -(choices[i] - 4)
        elif survey[i][0] == "C":
            help[1] += -(choices[i] - 4)
        elif survey[i][0] == "J":
            help[2] += -(choices[i] - 4)
        elif survey[i][0] == "A":
            help[3] += -(choices[i] - 4)
        elif survey[i][0] == "T":
            help[0] -= -(choices[i] - 4)
        elif survey[i][0] == "F":
            help[1] -= -(choices[i] - 4)
        elif survey[i][0] == "M":
            help[2] -= -(choices[i] - 4)
        elif survey[i][0] == "N":
            help[3] -= -(choices[i] - 4)

    answer = ''

    if help[0] >= 0:
        answer = answer + 'R'
    else:
        answer = answer + 'T'

    if help[1] >= 0:
        answer = answer + 'C'
    else:
        answer = answer + 'F'

    if help[2] >= 0:
        answer = answer + 'J'
    else:
        answer = answer + 'M'

    if help[3] >= 0:
        answer = answer + 'A'
    else:
        answer = answer + 'N'

    return answer