import sys
import os
print(os.getcwd())
sys.stdin = open("./input.txt", "rt")

#############
# Bottom Up #
#############
# n = int(input())
n = 7
dy = [0]*(n+1)

# 직관적으로 알 수 있는 부분 초기화
dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])

############
# Top Down #
############
def DFS(len):
    # 기록되어있으면 추가적으로 DFS 하지말고(가지뻗지 말고) 바로 return
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        # 기록테이블을 이용한다 -> DFS
        # 기록테이블을 이용하지 않는다 -> 단순 재귀
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]
    
if __name__ == "__main__":
    n = int(input())
    # n = 35
    dy = [0] * (n+1)
    print(DFS(n))