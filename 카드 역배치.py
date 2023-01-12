import sys
sys.stdin = open("algorithm/input.txt", "rt")

card = [i+1 for i in range(20)]
for _ in range(10):
    a, b = list(map(int, input().split()))
    card[a-1:b] = cardb-1:a-2:-1]
    print(card)
    # print(card[:a-1])
# a, b = 5, 10
# card = card[:a-1] + card[b:a-2:-1] + card[b+1:]
print(card)