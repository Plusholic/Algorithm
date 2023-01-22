import sys
sys.stdin = open("algorithm/input.txt", "rt")

string = input()
# cnt = 0
# # last = string[0]
# tmp = []
# eq = ['+', '-']#, '*', '/']
# eq_2 = ['*', '/']
# eq_3 = ['(', ')']
# res = []
stack = []
# for idx, str_ in enumerate(string):
    
#     if str_ in eq and string[idx+1] in eq_3: # 더하기 뺴기 괄호
#         res.append(str_)
#     elif str_ in eq_2 and string[idx+1] in eq_3: # 곱하기 나누기 괄호
#         if stack:
#             res.append(stack.pop())
#     # print(res, stack, tmp)
#     if str_ in eq:
#         stack.append(str_)
#     elif str_ in eq_2:
#         print(stack)
#         while stack:
#             res.append(stack.pop())
#         stack.append(str_)
#     elif str_ in eq_3:
#         tmp.append(str_)
#         cnt += 1    
#     else: # 숫자면 res에 추가
#         res.append(str_)
#     # print(str_, res, stack, tmp)
    

#     if len(tmp) == 2:
#         while stack:
#             res.append(stack.pop())
#         cnt = 0
#         tmp.clear()
# for st in stack[::-1]:
#     res.append(st)

# print(''.join(map(str, res)))


# 답 2
res = ''
for str_ in string:
    if str_.isdecimal():
        res += str_
        
    else:
        if str_ == '(':
            stack.append(str_)
        elif str_ == '*' or str_ =='/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(str_)
        elif str_ == '+' or str_ =='-':
            while stack and (stack[-1] != '('): # 여는 괄호 전까지만 다 추가
                res += stack.pop()
            stack.append(str_)
        elif str_ == ')':
            while stack and (stack[-1] != '('): # 여는 괄호 전까지만 다 추가
                res += stack.pop()
            stack.pop() # '(' 전까지만 while 문이 돌면서 pop 시키니까, 괄호 닫을때는 없애줘야함
            
while stack:
    res += stack.pop()
    
print(res)
