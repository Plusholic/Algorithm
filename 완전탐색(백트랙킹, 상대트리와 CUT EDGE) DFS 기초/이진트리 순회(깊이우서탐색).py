import sys
sys.stdin = open('algorithm/input.txt', 'r')

# 깊이 우선 탐색 DFS
# 재귀를 이용해서 깊이 우선 탐색을 배우는 것이 목적임.

def DFS(v):
    if v > 7:
        return # 함수 종료
    else:
         # 왼쪽과 오른쪽 가기 전에 먼저 출력 -> 전위순회 방식
        # print(v, end = ' ')
        # DFS(v * 2) # 왼쪽 노드 방문
        # DFS(v * 2 + 1) # 오른쪽 노드 방문
        
         # 왼쪽 처리하고 출력하고 오른쪽 출력 -> 중위순회 방식
        # DFS(v * 2) # 왼쪽 노드 방문
        # print(v, end = ' ')
        # DFS(v * 2 + 1) # 오른쪽 노드 방문

         # 왼쪽 처리하고 출력하고 오른쪽 출력 -> 후위순회 방식
        DFS(v * 2) # 왼쪽 노드 방문
        DFS(v * 2 + 1) # 오른쪽 노드 방문
        print(v, end = ' ')
        
if __name__ =="__main__":
    DFS(1)