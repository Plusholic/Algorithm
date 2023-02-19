import sys
sys.stdin = open('algorithm/input.txt', 'r')

N, M = map(int, input().split())

adj = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    
    n, e, v = map(int, input().split())
    adj[n-1][e-1] = v
    
for row in adj:
    for i in row:
        print(i, end=' ')
    print()