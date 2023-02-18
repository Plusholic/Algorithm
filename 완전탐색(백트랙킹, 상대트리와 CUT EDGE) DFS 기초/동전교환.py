
import sys
sys.stdin = open('algorithm/input.txt', 'r')

def DFS(L, sum):
    global res
    # CUT EDGE
    if L > res:
        return
    if sum > M:
        return
    if sum == M:
        if L < res:
            res = L
    
    else:
        for i in range(N):
            DFS(L+1, sum + a[i])
        

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    M = int(input())
    res = 247000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)