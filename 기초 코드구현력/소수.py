import sys
sys.stdin = open("algorithm/input.txt", "rt")

# 자연수의 갯수
# N = int(input())
# res = 0
# for num in range(2,N+1):
#     cnt = 0
#     for i in range(2, num+1):
#         # 나머지가 0인게 하나만 있어야함.
#         if num % i == 0:
#             cnt += 1
            
#     if cnt == 1:
#         res += 1
# print(res)
# 소수의 갯수 출력


# 선생님 풀이
N = int(input())
ch=[0]*(N+1) # 여기서 갯수
cnt = 0

for i in range(2, N+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
            
print(cnt)

# 짝수는 표시해서 걸러내기

