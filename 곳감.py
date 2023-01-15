import sys
sys.stdin = open("algorithm/input.txt", "rt")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
# 이거 모르겠다.
# 회전명령 2 0 3
# -> 2행 0:3 까지를 [2:] 로 미룸
# M개의 회전명령을 실행하고
# for _ in range(M):
#     row, d, loc = map(int, input().split())
#     if d == 1:
#         tmp = grid[row-1][:loc-1]
#         grid[row-1][:loc] = grid[row-1][:loc-1]
#         grid[row-1][:loc-1] = tmp
#     else:
#         tmp = grid[row-1][:loc:]
#         grid[row-1][:loc:] = grid[row-1][:loc:]
#         grid[row-1][:loc:] = tmp


########## 선생님 답

import sys
sys.stdin = open("algorithm/input.txt", "rt")

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
for i in range(M):
    h, t, k = map(int, input().split())
    if t == 0: # 왼쪽방향 회전
        for _ in range(k):
            print(a[h-1])
            a[h-1].append(a[h-1].pop(0)) # 제일 앞의 자료를 하나 빼내고(pop(0)), 그 값을 제일 뒤에 추가
            print(a[h-1])
            print(' ')
            # pop 함수는 빼낸 값을 반환하고, 원래 리스트는 하나 빠진 값으로 업데이트됨
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) # 제일 뒤의 자료를 꺼내서(pop()) 앞에 넣음.
            
for x in a:
    print(x)
    
res = 0
s = 0
e = N-1
for i in range(N):
    for j in range(s, e+1):
        res +=a[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
        
print(res)