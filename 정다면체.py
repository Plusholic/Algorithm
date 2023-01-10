import sys
sys.stdin = open("algorithm/input.txt", "rt")

# 정N면체, 정M면체의 주사위
N, M = list(map(int, input().split()))

# 눈의 합 계산
res = []
for n in range(1, N+1):
    for m in range(1, M+1):
        res.append(n+m)

res = sorted(res)
# print(res)
# 그중 가장 확률이 높은 숫자를 출력
res_dict = {}
cnt = 0
for idx, val in enumerate(res[:-1]):
    if val == res[idx+1]:
        cnt += 1
        
    elif val != res[idx+1]:
        res_dict[val] = cnt
        cnt = 0

for val in res_dict.keys():
    if res_dict[val] == max(res_dict.values()):
        print(val, end=' ')
        

        
# 선생님 답
import sys
sys.stdin = open("algorithm/input.txt", "rt")

# 정N면체, 정M면체의 주사위
N, M = list(map(int, input().split()))
cnt = [0]*(N+M+3) # 3은 그냥 크기 넉넉하게 잡은것.
for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1 # 이렇게 저장하면 i+j라는 눈금의 합을 인덱스로 해서, 나온 횟수만큼 값이 저장됨.
        
max = -214700000
for i in range(N+M+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(N+M+1):
    if cnt[i] == max:
        print(i, end=' ')