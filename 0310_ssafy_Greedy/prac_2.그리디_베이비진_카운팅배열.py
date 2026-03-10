import sys
sys.stdin = open('0310_ssafy_Greedy/input.txt', 'r')
#0부터 9까지 숫자 카드 4세트를 섞은 후 , 6개의 카드를 고른다.

def find(card, p1_card, p2_card):
        for idx, val in enumerate(card):
            if idx % 2 == 0:
                p1_card[val] += 1
            else: p2_card[val] += 1

            for i in range(10):
                if p1_card[i] >= 3:
                    return 1
                elif p1_card[i] >= 1 and p1_card[i+1] >= 1 and p1_card[i+2] >= 1:
                    return 1
                elif p2_card[i] >= 3:
                    return 2
                elif p2_card[i] >= 1 and p2_card[i+1] >= 1 and p2_card[i+2] >= 1:
                    return 2
        return 0

#게임을 하면 1, 2 교대로 한 장씩 카드를 가져가며,
# 6장 채우기 전에 먼저 run or triplet 되면 끝
#두 사람이 가져가게 되는 순서대로 12장 카드 정보 주어질 때,
# 승자를 알아내는 프로그램
# 플레이이어 1, 2 / 무승부라면 0
T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    p1_card = [0] * 13  #0 2 4 6 8 10
    p2_card = [0] * 13 # 1 3 5 7 9 11
    #런이냐 트립렛이냐
    #012, 123, 234, 345 이렇게 확인 / 하나 빼고 하나 추가

    #6개의 카드를 고르면 끝
    #카드의 종류는 0 - 9, 10가지
    result = 0

    print(f'#{tc} {find(card, p1_card, p2_card)}')
            
