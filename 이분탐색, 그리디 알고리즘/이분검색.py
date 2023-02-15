import sys
sys.stdin = open("algorithm/input.txt", "rt")

# # N개 숫자 입력으로주어짐
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# # N개 수를 오름차순 정렬
sorted_list = [0] * N
for idx, num_1 in enumerate(numbers):
    cnt = 0
    # numbers에 있는 다른 숫자들과 비교해서 num_1이 몇번이나 더 큰지
    # 큰 갯수만큼 sorted_list의 위치에 넣어줌
    for num_2 in numbers:
        if num_1 > num_2:
            cnt += 1
    sorted_list[cnt] = num_1

numbers.sort()
sorted_list = numbers
for idx, num in enumerate(sorted_list):
    if num == M:
        print(idx+1) # 답은 0번째가 아닌 1번째부터 시작
        break
    
# enumerate 속도?


# 선생님 답
# 맨 왼쪽 lt, 맨 오른쪽을 가르키는 rt 가 필요. 두개의 포인트 변수 lt~rt는 데이터의 범위
# mid = (lt + rt) // 2  
# 아이디어는 업다운. 중간을 찍으면 전체 범위의 절반으로 줄어듦.


N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 오름차순 정렬
numbers.sort()
lt = 0
rt = N-1

while lt <= rt:
    mid = (lt + rt) // 2
    if numbers[mid] == M:
        print(mid+1)
        break
    elif numbers[mid] > M:
        rt = mid -1
    else:
        lt = mid + 1
    

