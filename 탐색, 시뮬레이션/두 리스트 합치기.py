import sys
sys.stdin = open("algorithm/input.txt", "rt")

# 첫 번째 리스트의 크기
# n개의 리스트 원소가 오름차순
# 두 번째 리스트의 크기
# m개의 리스트 원소가 오름차순

N = int(input())
list_1 = list(map(int, input().split()))
M = int(input())
list_2 = list(map(int, input().split()))

print(sorted(list_1 + list_2)) 

# 선생님 답

# sort는 시간복잡도가 nlogn 이다.
# 이미 정렬되어있기 때문에 n번만에 답을 찾을 수 있다.

N = int(input())
list_1 = list(map(int, input().split()))
M = int(input())
list_2 = list(map(int, input().split()))
p1 = p2 = 0
c = []
# p1이나 p2 둘중 하나만 자료를 다 처리하면 끝남
while p1 < N and p2 < M:
    if list_1[p1] <= list_2[p2]:
        c.append(list_1[p1])
        p1 += 1
    
    else:
        c.append(list_2[p2])
        p2 += 1
        
if p1 < N: # 이러면 p1이 N까지 못 가고 남은것
    c = c+list_1[p1:]
if p2 < M:
    c = c+list_2[p2:]
print(c)
