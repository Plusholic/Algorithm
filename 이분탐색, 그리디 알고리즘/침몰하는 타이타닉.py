import sys
sys.stdin = open("algorithm/input.txt", "rt")

N, M = map(int, input().split())
weights = list(map(int, input().split()))

# N개로구성된 몸무게 수열, 각 승객의 몸무게는 M을 넘지 않는다. -> 탈출 못하는 경우는 없음
# N명 승객이 타고 있는데, 구명보트를 타고 탈출해야함. 구명보트는 2명 이하로만 탈 수 있음
# 보트 한개에 탈 수 있는 총 무게는 M kg 이하
# 구명보트의 최소 개수 출력

# 140 이하
# 아 나는 실수함. 순서대로 태우려고만 했음. sort한 다음 사람이 아니라 몸무게 가장 작은 사람이 탈 수 있는지를 봐야함.


weights.sort()
cnt = 0

while weights:
    # 양쪽을 짝짓다가 마지막 한명만 남았을 때, 아래쪽 코드에서는 에러가 남
    if len(weights) == 1:
        cnt += 1
        break
    
    if weights[0] + weights[-1] > M:
        weights.pop()
        cnt += 1
    else:
        weights.pop(0)
        weights.pop()
        cnt += 1
    
print(cnt)


####


import sys
from collections import deque
sys.stdin = open("algorithm/input.txt", "rt")

N, M = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
weights = deque(weights)
cnt = 0

while weights:
    # 양쪽을 짝짓다가 마지막 한명만 남았을 때, 아래쪽 코드에서는 에러가 남
    if len(weights) == 1:
        cnt += 1
        break
    
    if weights[0] + weights[-1] > M:
        weights.pop() # 맨 뒷 자료에서 나감
        cnt += 1
    else:
        weights.popleft() # deque 자료구조가 조금 더 효율적임.
        weights.pop()
        cnt += 1
    
print(cnt)