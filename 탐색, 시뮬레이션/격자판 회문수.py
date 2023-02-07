import sys
sys.stdin = open("algorithm/input.txt", "rt")
grid = [list(map(int, input().split())) for _ in range(7)]

# 5자리 회문수가 몇개 있는지 구하는 프로그램.
# 가로방향 또는 세로방향으로 길이 5자리 회문수.
# 회문은 앞으로 읽으나 뒤로 읽으나 같아야 함.

# 가로방향 회문
# 행, 열중 하나를 고정
cnt = 0
for stand in range(0, 7):
    # 행, 열 중에서 1~3까지 인덱스가 가야함.
    for idx in range(7//2):
        if all(grid[stand][idx+i] == grid[stand][idx+4-i] for i in range(7//2-1)):
            cnt += 1
        if all(grid[idx+i][stand] == grid[idx+4-i][stand] for i in range(7//2-1)):
            cnt += 1

print(cnt)

# 선생님 답

import sys
sys.stdin = open("algorithm/input.txt", "rt")
grid = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = grid[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        
        # for else 구문
        # 열 고정
        for k in range(2):
            if grid[i+k][j] != grid[i+5-k-1][j]:
                break
        else:
            cnt += 1
print(cnt)