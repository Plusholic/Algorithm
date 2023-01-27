import sys
sys.stdin = open("algorithm/input.txt", "rt")

N, M = map(int, input().split())
pat = list(map(int, input().split()))


# 의사가 한명

# 접수한 순서대로 목록에서 제일 앞의 환자

from collections import deque
pat = deque(pat)
obj = pat[M]
cnt = 0
while pat:
    
    cur = pat.popleft()
    for i in range(len(pat)):
        if cur < pat[i]:
            # 하나라도 현재값보다 크면 break
            pat.append(cur)
            # print(pat)
            break
    else:
        cnt += 1
        if obj == cur:
            print(cnt)


# 같은 위험도 처리?? 말이 애매한
# 선생님 답

import sys
sys.stdin = open("algorithm/input.txt", "rt")

N, M = map(int, input().split())
pat = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
pat = deque(pat)
cnt = 0
while True:
    cur = pat.popleft()
    # any 사용해서 하나라도 조건을 만족하면 True
    if any(cur[1] < x[1] for x in pat):
        pat.append(cur)
    else:
        cnt += 1
        if cur[0] == M:
            print(cnt)
            break