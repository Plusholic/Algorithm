import sys
sys.stdin = open("algorithm/input.txt", "rt")


def reverse(x):
    res = 0
    n = len(str(x))
    # 자릿수만큼 루프를 돌면서 나머지에 10 ** (n-1)을곱해줌
    for i in range(n, 0, -1):
        
        res += (x % 10) * (10 ** (i-1))
        x = x // 10
    return res

def isPrime(x):
    # 1은 걸러내야 하니까 2부터, 자기자신-1까지 루프
    cnt = 0
    for n in range(2, x):
        if x % n == 0:
            cnt += 1
    
    # 1이랑 자기자신으로 안 나눠주기때문에, 0일때만 소수
    if cnt == 0:
        res = True
    else:
        res = False
    return res

#N개의 자연수 입력
N = int(input())
N_list = list(map(int, input().split()))

# 자연수를 뒤집은 후 소수이면 출력
for num in N_list:
    num = reverse(num)
    if isPrime(num):
        print(num, end=' ')
        
        
# 선생님 답


        
# def isPrime(x):
#     # x 가 1이면 종료
#     if x == 1:
#         return False
#     # 약수가 발견되면 종료
#     for i in range(2, x//2+1):
#         if x%i == 0:
#             return False
#     # 1도 아니고 약수도 없으면 종료
#     else: # for else 구문
#         return True
        
# def reverse(x):
#     res = 0
#     while x > 0:
#         t = x % 10 # x의 1의자리 숫자가 t
#         res = res * 10 + t
#         x = x//10
#     return res
        
# #N개의 자연수 입력
# N = int(input())
# N_list = list(map(int, input().split()))

# for x in N_list:
#     tmp = reverse(x)
#     if isPrime(tmp):
#         print(tmp, end=' ')
