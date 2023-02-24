import sys
sys.stdin = open('algorithm/input.txt', 'r')

# 이렇게 하면 무한 실행됨
def DFS(x):
    if x > 0:
        print(x) # 11 10 9 ...
        DFS(x-1)
        print(x, end=' ') # 1 2 3 ... 스택 자료구조를 활용하기 때문에.
        # print(x)
        

if __name__ == "__main__":
    n = int(input())
    DFS(n)