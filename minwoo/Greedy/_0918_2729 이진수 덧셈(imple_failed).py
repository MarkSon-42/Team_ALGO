# boj 2729 b1 이진수 덧셈

t = int(input())
answer = []
b1, b2 = map(int, input().split())
#  1001101
#    10010
b1_len = len(b1)
b2_len = len(b2)
maxlen = 0
if b1_len >= b2_len:
    maxlen = b1_len
else:
    maxlen = b2_len

for i in range(maxlen):
    if str(b1)[:-i-1] == '1' or str(b2)[-i-1] == '1':
        answer.append(1)
    elif str(b1)[:-i-1] == '0' and str(b2)[-i-1] == '0':
        answer.append(0)
    else:
        answer.append(0)
        up = 1