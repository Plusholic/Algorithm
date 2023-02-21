import sys
sys.stdin = open('algorithm/input.txt', 'r')

def DFS(L, s, sum):
    global cnt
    if L == K: # 종료조건을 추가해야 함. 

        if sum % M == 0:
            cnt += 1
        return
        
    else:
        for i in range(s, N) :
            DFS(L+1, i+1, sum+a[i])


if __name__ == "__main__":
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    M = int(input())

    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
    
    
