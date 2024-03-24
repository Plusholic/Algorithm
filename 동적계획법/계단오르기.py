# 네트워크 선 자르는것과 똑같음

def DFS(len):
    
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return dy[len]
    else:
        
        dy[len] = DFS(len-1) + DFS(len-2)
    
    return dy[len]
 
if __name__ == "__main__":
    
    # n = int(input())
    n = 7
    dy = [0] * (n+1)
    dy[1] = 1
    dy[2] = 2
    dy[3] = 3
    print(DFS(n))