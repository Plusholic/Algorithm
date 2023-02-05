import sys
sys.stdin = open("algorithm/input.txt", "rt")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 격자에 한 그루의 사과나무
# 다이아몬드 모양의 격자판만 수확하고, 나머지 격자는 남겨둠
# 수확한 총 사과의 갯수 -> 다이아몬드 모양 격자판 숫자 합.

loc = N//2
for i in range(N):
    if loc-i > 0:
        grid[i][0:loc-i] = [0] * (loc-i)
        grid[i][-loc+i:] = [0] * (loc-i)
    elif loc-i < 0:
        grid[i][0:i-loc] = [0] * (i-loc)
        grid[i][-i+loc:] = [0] * (i-loc)

sum_ = 0
for row in grid:
    for j in row:
        sum_ += j

print(sum_)

## 선생님 답
import sys
sys.stdin = open("algorithm/input.txt", "rt")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 다이아몬드 모양으로 탐색하면서 sum에 더해주면 됨
sum_ = 0
s = e = N//2
for i in range(N): # 행
    for j in range(s, e+1): # start, end 위치
        sum_ += grid[i][j]
        
    if i < N // 2:
        s -= 1
        e += 1
    
    else:
        s += 1
        e -= 1

print(sum_)
        
        


