import sys
sys.stdin = open("algorithm/input.txt", "rt")
# N명의 학생 수학성적
N = int(input())
scores = list(map(int, input().split()))

# 학생 성적의 평균(소수 첫째자리 반올림)

mean_score = 0
for score in scores:
    mean_score += score
mean_score = round(mean_score/N)

# 평균에 가장 가까운 학생은 몇 번째 학생인지
mrs = 10000
res_idx, res_score = [], []
for idx, score in enumerate(scores):
    if mrs >= abs(mean_score - score):
        mrs = abs(mean_score - score)
        res_idx.append(idx)
        res_score.append(score)

base_score = 0
for idx, score in enumerate(res_score):
   if  base_score < score:
       base_score = score
       res_idx_2 = idx

print(mean_score, res_idx[res_idx_2]+1)
# # 답이 2개일 경우 성적이 높은 학생의 번호


###########################
#########선생님 답##########
############################

import sys
sys.stdin = open("algorithm/input.txt", "rt")
# N명의 학생 수학성적
N = int(input())
scores = list(map(int, input().split()))
mean_score = round(sum(scores)/N)
min = 10000
for idx, score in enumerate(scores):
    tmp = abs(score-mean_score)
    if tmp < min:
        min=tmp
        res_score = score
        res = idx + 1
        
    elif tmp == min:
        if score > res_score:
            res_score = score
            res = idx + 1
            
print(mean_score, res)




# round는 round half even 방식을 택한다.
# 정확하게 half 지점에 잇으면 even(짝수)로 근사함.

a = 4.500
print(round(a)) # 4가 나옴

a = 4.501
print(round(a)) # 5가 나옴 -> 정확한 half가 아니기 때문

## round 함수를 쓰면 안됨 ##

a = 66.6
a += 0.5
a = int(a)
print(a)
