import sys
sys.stdin=open("algorithm/input.txt", "rt")

N = int(input())
# N개의 문자열 데이터 입력

for _ in range(N):
    str_1 = str(input())
    str_2 = ''
    for i in range(len(str_1)-1, -1, -1):
        # print(i)
        str_2 += str_1[i]
    
    # 앞에서 읽을때나 뒤에서 읽을때나 같은 경우 -> Yes
    if str_2 == str_1:
        print('YES')
    # 회문 문자열이 아니면 No
    else:
        print('NO')
        
# 선생님 답_1

import sys
sys.stdin=open("algorithm/input.txt", "rt")

N = int(input())
# N개의 문자열 데이터 입력

for i in range(N):
    str_1 = input()
    str_1 = str_1.upper() # upper로 전부 대문자 처리(B.C 대소문자 구별 x)
    size = len(str_1)
    
    # level의 경우 첫번째 l과 마지막 l, 두번째 e와 마지막 e만 비교하면 됨
    # 반만 돌아도 됨
    for j in range(size // 2):
        if str_1[j] != str_1[-1-j]: # 인덱스를 -1, -2 등등으로도 접근할 수 있음
            print("#%d NO" %(i+1))
            break
        
    else:
        print("#%d YES" % (i+1))
        

# 선생님 답_2

import sys
sys.stdin=open("algorithm/input.txt", "rt")

N = int(input())
# N개의 문자열 데이터 입력

for i in range(N):
    str_1 = input()
    str_1 = str_1.upper() # upper로 전부 대문자 처리(B.C 대소문자 구별 x)
    size = len(str_1)
    
    if str_1 == str_1[::-1]: # str_1[::-1]은 리버스가 됨
        print("#%d Yes" %(i+1))
    else:
        print("#%d No" %(i+1))
        
        

a = [1,2,3,4,5]
print(a[::-1])
