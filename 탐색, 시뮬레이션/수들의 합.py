
import sys
sys.stdin = open("algorithm/input.txt", "rt")

N, M = map(int, input().split())
seq = list(map(int, input().split()))
res = 0
for i in range(M):
    for j in range(i, M):
        if sum(seq[i:j+1]) == N:
            res += 1
        
print(res)

# # 선생님 답
# # 순서대로 더하다가 N과 같아지면 정지 cnt +=1 하고 정지, 다음 루프로 넘어감
# # 다음 인덱스를 더하면 N보다 커지기 때문

lt, rt = 0, 1
res = 0
tot = seq[0]
while True:
    if tot < M:
        if rt < N:
            tot += seq[rt]
            rt += 1
        else: # rt >= n 일때
            break

    elif tot == M:
        res += 1
        tot -= seq[lt]
        lt += 1
        
    else:
        tot -= seq[lt]
        lt += 1

print(res)