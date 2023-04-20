# import sys
# sys.stdin = open("algorithm/input.txt", "rt")
# N = int(input())
# A_list = list(map(int, input().split()))
# B_list = list(map(int, input().split()))
# C_list = list(map(int, input().split()))

# # 3개의 주사위를 던져서 상금을 받는 게임
# def Count(x):
#     cnt_list = [0] * len(x)
#     # cnt = 0
#     for idx, num1 in enumerate(x):
#         cnt = 1
#         for num2 in x[idx+1:]:
#             if num1 == num2:
#                 cnt += 1           
#         cnt_list[idx] = cnt
#     return cnt_list


# res_list = []
# for num_list in [A_list, B_list, C_list]:
#     cnt_list = Count(num_list)

#     # 같은 눈이 3개 나오면 10000원 + 같은눈 * 1000원
#     for idx, num in enumerate(cnt_list):
#         if num == 3:
#             res = 10000 + num_list[idx] * 1000
#             # 더이상 res가 업데이트 되지 않도록 for문 중단
#             break
#         # 같은 눈이 2개 나오면 1000원 + 같은 눈 * 100원
#         elif num == 2:
#             res = 1000 + num_list[idx] * 100
#             break
#         # 모두 다른 눈이 나오면 그 중 가장 큰 눈 * 100원
#         elif num == 1:
#             res = max(num_list) * 100
#             break
#     res_list.append(res)

# print(max(res_list))


# 선생님 답
import sys
sys.stdin = open("algorithm/input.txt", "rt")
N = int(input())
res = 0
for i in range(N):
    tmp = input().split() # 문자화된 숫자의 리스트
    tmp.sort()
    a, b, c = map(int, tmp) # a, b, c를 숫자화
    
    if a == b and b == c: # 3개 다 같은 경우
        money = 10000 + a * 1000
    
    # 계산할때 하나의 눈으로 변수잡기 위해서 나눠줌.
    elif a == b or a == c:
        money = 1000 + (a * 100)
        
    elif b == c:
        money = 1000 + (b * 100)
    
    else:
        money = c * 100 # sort를 했기 때문에
        
    if money > res:
        res = money

print(res)
        
    
