import sys
sys.stdin = open("algorithm/input.txt", "rt")
N = int(input())
scores = list(map(int, input().split()))

res_list = []
last_score = scores[0]
if last_score == 1:
    res_list.append(1)
else:
    res_list.append(0)
    
for score in scores[1:]:
    
    if score == 1:
        if score == last_score:
            res += 1
            res_list.append(res)
        else:
            res = 1
            res_list.append(1)
        
    elif score == 0:
        res = 0
        res_list.append(res)
    
    last_score = score

print(sum(res_list))

# 선생님 답

import sys
sys.stdin = open("algorithm/input.txt", "rt")
N = int(input())
scores = list(map(int, input().split()))

sum = 0
cnt = 0
for score in scores:
    if score == 1:
        cnt += 1 # 가중치 증가
        sum += cnt # 가중치를 증가시키면서 계속 더해줌
    
    else:
        cnt = 0

print(sum)
    