import sys
sys.stdin = open('algorithm/input.txt', 'r')


def DFS(L, sum):
    global max_sum

    # 4번 5번에서 너무 많은 시간이 걸림 -> 이거 말고도 다른 종료조건이 필요함
    if max_sum < sum:
        max_sum = sum
    
    if L == N:
        return sum
    
    if sum + W[L] > C:
        return sum
    
    else:
        DFS(L+1, sum + W[L])
        DFS(L+1, sum)


if __name__ == '__main__':
    W = []
    C, N = map(int, input().split())
    max_sum = 0
    
    for _ in range(N):
        W.append(int(input()))
    DFS(0, 0)
    print(max_sum)
#### 선생님 답


import sys
from collections import deque
sys.stdin = open('algorithm/input.txt', 'r')

def DFS(L, sum, tsum):
    global res
    
    # total - tsum 이 앞으로 판단해야 할 바둑이들의 무게
    # tsum이 지금까지 판단한 바둑이들의 무게
    if sum + (total - tsum) < res:
        return
    
    # sum이 무게제한을 넘어가면 안됨
    if sum > C:
        return
    
    if L == N:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__ == "__main__":
    C, N = map(int, input().split())
    a = [0] * N
    res = -2147000000
    for i in range(N):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(res)
