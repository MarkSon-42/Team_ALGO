a = input()
b = []
for i in a:
    if i == '7':
        b.append('111')
    elif i == '6':
        b.append('110')
    elif i == '5':
        b.append('101')
    elif i == '4':
        b.append('100')
    elif i == '3':
        b.append('011')
    elif i == '2':
        b.append('010')
    elif i == '1':
        b.append('001')
    elif i == '0':
        b.append('000')

answer = list(''.join(b))
while answer and answer[0] == '0':
    answer.pop(0)
if answer:
    print(''.join(answer))
else:
    print(0)