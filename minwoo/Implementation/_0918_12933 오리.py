#  오리쉑.. 'quack'의 최소 개수를 찾으면 된다.
#  순서가 같아야 한다
#  qquuaacckk -> 2마리

sounds = input()
cnt = 0

# ['quak', 'qu', 'q']...

# 이런식으로 채워나가면 되지않을까?

# duck_sound = ['q', 'u', 'a', 'c', 'k']
duck_stack = [['']]

for c in sounds:
    for i in range(5):
        if c == 'q':
            pass
