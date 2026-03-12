import sys
sys.stdin = open('0312_ssafy_Backtracking2/input.txt', 'r')

#--------------------------------------------
# N = int(input())

# card = []
# for _ in range(N):
#     card.append(int(input()))

# card_plus = []
# total = 0
# while len(card) > 1:
#     card.sort()
#     card_plus.append(card[0] + card[1])
#     total += card.pop(0)
#     total += card.pop(0)

# print(sum(card_plus) + card[-1] + total)

##시간초과 코드 ----------------------------


import heapq, sys

input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += a+b
    heapq.heappush(heap, a+b)

print(result)