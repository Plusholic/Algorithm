def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
            
    
def solution(n, k):

    res = ''
    while True:
        res = str(n%k) + res
        n = n // k
        
        if n < k:
            res = str(n%k) + res 
            break
    
    res = res.split('0')
    # print(res)
    cnt = 0
    # print(res)
    for w in res:
        print(w)
        if len(w) == 0:
            continue
        if int(w) < 2:
            continue
        if is_prime(int(w)):
            cnt += 1
    
    return cnt