import sys
sys.stdin = open("algorithm/input.txt", "rt")

N = int(input())
# num_1, num_2, num_3 = list(map(str, input().split()))
num_list = list(map(str, input().split()))

val_list = [0] * N
for j in range(len(num_list)):
    for i in num_list[j]:
        val_list[j] += int(i)

for idx, val in enumerate(val_list):
    if val == max(val_list):
        print(num_list[idx])
        
# 선생님 답
import sys
sys.stdin = open("algorithm/input.txt", "rt")

N = int(input())
num_list = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x%10
        x = x//10 # 미쳤다 계속 나눠서 나머지를 계속 더하는 방식으로 할 수 있구나.
    return sum

max = -2147000000

for num in num_list:
    tot = digit_sum(num)
    if tot > max:
        max = tot
        res = num
        
print(res)
