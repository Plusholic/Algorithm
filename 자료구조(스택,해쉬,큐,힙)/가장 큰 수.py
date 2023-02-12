import sys
sys.stdin = open("algorithm/input.txt", "rt")

num, m = map(int, input().split())
num = list(map(int, str(num))) # str로 바꾸면 idx로 하나하나 접근할 수가 있음.

stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
    
if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)

# STACK 자료구조

# Last In First Out
# 운동장의 구덩이라고 생각하면 됨
# 좁은 구덩이에 공이 여러개 빠지면 마지막에 빠진 공부터 빼내야함.
# 스택은 리스트를 이용. pop을 하면 맨 뒤의 자료가 빠지고, append를 하면 뒤의 자료를 추가함.


    
    
    
    