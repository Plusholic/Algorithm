import sys
from collections import deque
sys.stdin = open("algorithm/input.txt", "rt")

N = int(input())
word_list = []

for _ in range(N):
    word_list.append(input())

for _ in range(N-1):
    
    tmp = input()
    
    for idx, word in enumerate(word_list):
        if tmp == word:
            word_list.pop(idx) # 쓴거 pop
            
print(word_list[0])


## 선생님 답
# 해쉬 = 딕셔너리

import sys
from collections import deque
sys.stdin = open("algorithm/input.txt", "rt")

N = int(input())
p = dict()

for i in range(N):
    word = input()
    p[word] = 1

for i in range(N-1):
    word = input()
    p[word] -=1
    
for key, val in p.items():
    if val == 1:
        print(key)
        break