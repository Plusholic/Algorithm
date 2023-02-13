import sys
sys.stdin = open("algorithm/input.txt", "rt")

from collections import deque
must = input()
# must = deque(must)
N = int(input())
cnt = 0
for _ in range(N):
    seq = input()
    seq = deque(seq)
    
    tmp_1 = must[cnt]
    while seq:
        # print(tmp_1, seq, cnt)
        tmp_2 = seq.popleft()
        if tmp_1 == tmp_2:
            cnt += 1
            if cnt < len(must):
                tmp_1 = must[cnt]
        
    if cnt == len(must):
        print('Yes')
        cnt = 0
    else:
        print('No')
        cnt = 0

# 선생님 답

print(' ')
import sys
from collections import deque

sys.stdin = open("algorithm/input.txt", "rt")
must = input()
N = int(input())

for i in range(N):
    seq = input()
    dq = deque(must)
    
    for x in seq:
        # print(x, dq)
        if x in dq: # 필수과목인지 확인
            if x != dq.popleft(): # 맨 앞에 있는지 확인
                print('No')
                break
            
    else:
        # 전부 다  pop 되었으면 잘 짠것임.
        if len(dq) == 0:
            print('Yes')
        else:
            print('No')