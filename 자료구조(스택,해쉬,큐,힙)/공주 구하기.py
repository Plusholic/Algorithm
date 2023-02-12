import sys
sys.stdin = open("algorithm/input.txt", "rt")

N, K = map(int, input().split())

que = [i+1 for i in range(N)]
cnt = 0
tmp = []
while len(que) > 1:
    
    # cnt가 3이면 무조건 break 됨
    for _ in range(len(que)):
        cnt += 1
        
        if cnt == K:
            que.pop(0) # cnt == 3이면 맨 앞이 3번째니까 제거해줘야함.
            tmp = que + tmp
            cnt = 0
            break
        
        else:
            tmp.append(que.pop(0))

    que = tmp
    tmp = []
    
    if len(que) == K-1:
        while len(que) < K:
            fix = len(que)
            que = que + que
            if len(que) >= K:
                break
        que.pop(K-1) # 2개면 3번째는 맨 앞이니까 제거
        que = que[fix:]
# 4 7 7
print(que[0])


# Que 자료구조 : First in First Out
# deque 자료구조 사용
# 일렬로 배열되어있는데, 제일 먼저 나온사람을 제일 뒤로 append 시키는 자료구조

from collections import deque
sys.stdin = open("algorithm/input.txt", "rt")
N, K = map(int, input().split())
dq = list(range(1, N+1))
dq = deque(dq)

while dq:
    # K-1 까지만 for을 돌려도 됨
    for _ in range(K-1):
        cur = dq.popleft() # 왼쪽에서 pop해서
        dq.append(cur) # 맨 오른쪽에 append
    # K번째에서는 그냥 pop만 하면 됨.
    dq.popleft()
    
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
        
        

