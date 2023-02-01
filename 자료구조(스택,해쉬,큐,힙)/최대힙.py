import sys
import heapq as hq
sys.stdin = open("algorithm/input.txt", "rt")

a = []
while True:
    n = int(input())
    if n == -1:
        break
    
    if n == 0: # 최소힙을 print 해야함.
        if len(a) == 0: # 힙에 아무것도 없다면
            print(-1)
        else: # heap에 데이터가 있으면 꺼내라.
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n) # a라는 리스트에 n값을 넣어라.
        # heapq는 기본적으로 최소힙으로 작동함
        # heappush를 하면 최소힙으로 만들어냄
        # heappop을 하면 root에서 하나 꺼내고 다시 최소힙으로 만듦
        
        # 최대힙을 만들기 위해서 음수를 넣은다음에, 출력할 때 -를 붙여서 해주면 됨.
        