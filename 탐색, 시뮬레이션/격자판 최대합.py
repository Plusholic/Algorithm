import sys
sys.stdin = open("algorithm/input.txt", "rt")

# 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장큰값

# 첫 줄에 자연수 N
N = int(input())
# 두 번째 줄부터 N 줄에 걸쳐 격자판이 주어짐
grid = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    grid.append(tmp)
    
##################
max_ = 0
# 각 행의 합

for i in range(N):
    sum_col = 0
    # 각 행의 합
    if max_ < sum(grid[i]):
        max_ = sum(grid[i])
    
    # 각 열의 합
    for j in range(N):
        sum_col += grid[j][i]
    if max_ < sum_col:
        max_ = sum_col
    
# 두 대각선의 합
sum_dia = 0
sum_dia_list = []
for i in range(N):
    sum_dia += grid[i][i]
if max_ < sum_dia:
    max_ = sum_dia

sum_dia = 0
for i in range(N):
    sum_dia += grid[i][N-1-i]
if max_ < sum_dia:
    max_ = sum_dia

    
# 최대값 출력
print(max_)


### 선생님 답
import sys
sys.stdin = open("algorithm/input.txt", "rt")


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)] # 이런식으로 사용 가능 체크
max_ = -2147000000 # 이런식으로 사용 가능 체크
for i in range(N):
    sum1 = sum2 = 0 # 이런식으로 사용 가능 체크
    for j in range(N):
        sum1 += grid[i][j] # 행 합
        sum2 += grid[j][i] # 열 합
    if sum1 > max_:
        max_ = sum1    
    if sum2 > max_:
        max_ = sum2

sum1=sum2=0
for i in range(N):
    sum1 += grid[i][i]
    sum2 += grid[i][N-1-i]
if sum1 > max_:
    max_ = sum1    
if sum2 > max_:
    max_ = sum2
    
print(max_)
