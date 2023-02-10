import sys
sys.stdin = open("algorithm/input.txt", "rt")
# N명의 학생 수학성적
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 0으로 패딩
grid.insert(0, [0] * (N+2))
grid.append([0] * (N+2))
for i in range(1, (N+1)):
    grid[i].insert(0, 0)
    grid[i].append(0)

# N x N 배열에서 상하좌우보다 큰 지점의 갯수
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if ((grid[i][j] > grid[i][j-1]) and (grid[i][j] > grid[i][j+1])  and (grid[i][j] > grid[i-1][j])  and (grid[i][j] > grid[i+1][j])):
            cnt += 1            
print(cnt)

## 선생님 답 ##

import sys
sys.stdin = open("algorithm/input.txt", "rt")
# N명의 학생 수학성적
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0] # 이렇게 초기화. 위치를 나타냄.
dy = [0, 1, 0, -1] # 

grid.insert(0, [0] * N)
grid.append([0] * N)
for x in grid:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(grid[i][j] > grid[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
            # all 함수 용법. 내부의 조건 모두가 참일때 참이 됨.
            # 총 for loop의 4번을 다 만족해야 참임.
            
print(cnt)