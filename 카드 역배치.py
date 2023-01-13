import sys
sys.stdin = open("algorithm/input.txt", "rt")


# # 1부터 20까지 쓰인 카드
# # [5 10] -> 1 2 3 4 10 9 8 7 6 5 11 12 ~
# cards = [i+1 for i in range(20)]

# for _ in range(10):
#     a, b = map(int, input().split())
#     if a != 1:
#         cards[a-1:b] = cards[b-1:a-2:-1]
#         print(cards)

#     # a가 1이면 cards[1:-1:-1] = [] 이 됨.
#     elif a == 1:
#         cards[a-1:b] = cards[b-1::-1]
#         print(cards)
        
### 선생님 답

cards = list(range(21))
print(cards)
for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        cards[a+i], cards[b-i] = cards[b-i], cards[a+i]

cards.pop(0) # 0번 인덱스를 없애버림
print(cards)