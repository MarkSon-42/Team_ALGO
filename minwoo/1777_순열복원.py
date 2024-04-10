# 세그먼트 트리 초기화 함수
def initialize(node, start, end):
    if start == end:
        seg[node] = 1
        return seg[node]
    seg[node] = initialize(node*2, start, (start+end)//2) + initialize(node*2 + 1, (start+end)//2+1, end)
    return seg[node]

# 세그먼트 트리에서 인덱스 찾는 함수
def find_index(node, start, end, value):
    if start == end:
        return start
    if value < seg[node*2 + 1]:
        return find_index(node*2 + 1, (start+end)//2 + 1, end, value)
    else:
        return find_index(node * 2, start, (start + end) // 2, value - seg[node * 2 + 1])

# 세그먼트 트리 업데이트 함수
def update_tree(node, start, end, idx):
    if not (start <= idx <= end):
        return
    seg[node] -= 1
    if start != end:
        update_tree(node*2, start, (start+end)//2, idx)
        update_tree(node*2 + 1, (start+end)//2 + 1, end, idx)

n = int(input())
sequence = list(map(int,input().split()))
seg = [0]*(4*n)
answer = [0]*n
initialize(1,0,n-1)
for i in range(n-1,-1,-1):
    idx = find_index(1,0,n-1,sequence[i])
    answer[idx] = i+1
    update_tree(1,0,n-1,idx)
for i in answer:
    print(i, end=' ')