import sys
sys.stdin = open("algorithm/input.txt", "rt")

# 숫자가 섞인 문자열
string = input()
int_list = []

# 문자랑 숫자가 섞여있는 문자열에서 숫자만 추출
for i in string:
    if i.isdigit():
        int_list.append(i)

# 그 순서대로 자연수를 만듦
# # 만들어진 자연수와 자연수의 갯수를 출력
print(int_list)
res = 0
for idx, num in enumerate(int_list):
    res += int(num) * 10 ** (len(int_list)-(idx+1))
print(res)

# 약수의 갯수
cnt = 0
for i in range(res):
    if res % (i+1) == 0:
        cnt += 1
print(cnt)


# 선생님 답

import sys
sys.stdin = open("algorithm/input.txt", "rt")

# 숫자가 섞인 문자열
string = input()
res = 0
for x in string:
    if x.isdecimal(): # 0부터 9까지의 숫자면 참이 됨 isdigit은 2^31 도 참으로 인식
        res = res * 10 + int(x) # 순서대로니까 10 곱하고 더해준걸 저장하고 다시 10곱한걸 더해주고 저장하면 됨
        
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
        
print(cnt)
    
