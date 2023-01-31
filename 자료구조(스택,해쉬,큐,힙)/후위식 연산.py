import sys
sys.stdin = open("algorithm/input.txt", "rt")

string = input()
stack = []
cnt, cnt_2 = 0, 0
res, fin = 0, 0
for str_ in string:
    
    if str_.isdecimal():
        stack.append(int(str_))
        
    else:
        
        if str_ == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
            
        elif str_ == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
            
        elif str_ == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
            
        elif str_ == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
            
print(stack[0])