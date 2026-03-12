import sys
sys.stdin = open('0312_ssafy_Backtracking2/input.txt', 'r')

# n장의 카드를 갖고있다.
# x번 카드와 y번 카드를 골라 두 장 수를 더한다.
# 계산한 값을 x번 카드와 y번 카드 두 장 덮어쓴다.

# m번 반복하면 끝난다.
# n장의 카드 모두 더한 것중 가장 최소

# 카드의 개수, 카드를 몇 번 합체하나
N, M = map(int, input().split())
card = list(map(int, input().split()))

# M번이 되면 종료 그리고 값을 다 더함
# 카드를 더할 때, 가장 작은 수를 2개 더한다.
# 근데 더한 값을 그 2개에 덮어씌운다.
# 그래서 매번 가장 작은 수 2개를 가져와야한다. 매번 정렬은 어렵다.

for i in range(M):
    card.sort()
    card[0], card[1] = card[0] + card[1], card[0] + card[1]

print(sum(card))

