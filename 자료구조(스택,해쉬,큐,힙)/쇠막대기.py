import sys
sys.stdin = open("algorithm/input.txt", "rt")

steels = str(input())

# 1. 여는 괄호를 만나면 stack에 쌓음
# 2. 닫는 괄호를 만날 때 앞에꺼가 여는 괄호면 레이저 -> 레이저라면 pop 해줌

stack = []
last = ''
res = 0
for steel in steels:
    
    if steel == '(':
        stack.append(steel)
        
    else:
        stack.pop()
        # 닫는거일때 앞이 여는거면 레이저임
        if last == '(':
            res += len(stack)
        
        # 닫는거일때 앞이 닫는거면 하나씩 pop 하고 갯수를 세줌
        else:
            res += 1
            
    last = steel
print(res)