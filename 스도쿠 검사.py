import sys
sys.stdin = open("algorithm/input.txt", "rt")

stoku = [list(map(int, input().split())) for _ in range(9)]

stride = 3
s, e = 0, stride
k = 0
cnt = 0
# 아니 뭐가 문제지
for _ in range(1, 1+stride):
    for _ in range(0, stride):
        kernel = stoku[0+k][s:e] + stoku[1+k][s:e] + stoku[2+k][s:e]
        if all(i in kernel for i in range(1, 10)):
            cnt += 1
        s += stride
        e += stride
    k += stride
    s, e = 0, 3

# if cnt == 9:
#     print('YES')
# else:
#     print('NO')

#### 선생님 답 ####

import sys
sys.stdin = open("algorithm/input.txt", "rt")

stoku = [list(map(int, input().split())) for _ in range(9)]

# 체크리스트를 만들어서 위치에 저장
# **** 스도쿠 값을 리스트의 위치로 사용 ****

def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1 # 열번호가 증가
            ch2[a[j][i]] = 1 # 행번호가 증가
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    
    for i in range(3):
        for j in range(3):
            ch3=[0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True
            

