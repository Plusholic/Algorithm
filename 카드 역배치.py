import sys
sys.stdin = open("algorithm/input.txt", "rt")


# 1부터 20까지 쓰인 카드
# [5 10] -> 1 2 3 4 10 9 8 7 6 5 11 12 ~

cards = [i+1 for i in range(20)]
# print(cards)
# print(cards[1::-1])
for _ in range(10):
    a, b = map(int, input().split())
    if a != 1:
        cards[a-1:b] = cards[b-1:a-2:-1]
        print(cards)

    elif a == 1:
        cards[a-1:b] = cards[b-1::-1]
        print(cards)
        
    # 5, 10
    # 4:10
    # 9:3
    # print(a, b)
    # for i in range(a, b):
    #     cards[i-1] = cards[b+a-(i-1)]
    #     print(cards)