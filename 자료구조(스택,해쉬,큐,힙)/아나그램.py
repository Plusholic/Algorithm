import sys
from collections import deque
sys.stdin = open("algorithm/input.txt", "rt")

s1 = input()
s2 = input()
count = dict()

# print(set(s1+s2))

for w in set(s1+s2):
    count[w] = 0

for w in s1:
    count[w] += 1    
for w in s2:
    count[w] -=1


# print(count)
for key, val in count.items():
    if val != 0:
        print('NO')
        break
else:
    print('Yes')
    
    
#### 답 2

import sys
from collections import deque
sys.stdin = open("algorithm/input.txt", "rt")

s1 = input()
s2 = input()

str1 = dict()
str2 = dict()

# get은 dict에 x가 없으면 0을 넣어라 있으면 그 키값의 val을 return해서 1을 더해라
for x in s1:
    str1[x] = str1.get(x, 0) +1
    
for x in s2:
    str2[x] = str2.get(x, 0) +1
    
for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')
    
#### 답 3 리스트로 풀기

import sys
from collections import deque
sys.stdin = open("algorithm/input.txt", "rt")

s1 = input()
s2 = input()

str1 = [0] * 52
str2 = [0] * 52

for x in s1:
    if x.isupper(): # 만약 대문자라면
        str1[ord(x)-65] +=1 # ascii number로 변환하는 함수, 대문자 시작이 65니까 0으로 만들어주기 위해서 65를 빼줌
    else:
        str1[ord(x)-71] +=1 # 소문자일때는 71을 빼줘야함.
        
        
for x in s2:
    if x.isupper(): # 만약 대문자라면
        str2[ord(x)-65] +=1 # ascii number로 변환하는 함수, 대문자 시작이 65니까 0으로 만들어주기 위해서 65를 빼줌
    else:
        str2[ord(x)-71] +=1 # 소문자일때는 71을 빼줘야함.
        
for i in range(52):
    if str1[i] != str2[i]:
        print('NO')
        break
else:
    print('YES')