import sys
sys.stdin = open('0310_ssafy_Greedy/input.txt', 'r')


def babygin(choice):
    cnt = 0
 
    x,y,z = choice[0], choice[1], choice[2]
    if x == y == z:
         cnt += 1
    elif x == y-1 == z-2:
         cnt += 1
 
    return cnt == 1

def recur(cnt, subset, p):
    global result
    if cnt == 3:
        # print(*subset)
        if babygin(subset):
            result = True
        return
    
    for i in range(len(p)):
        if used[i] == 1:
            continue
        used[i] = 1
        recur(cnt+1, subset+[p[i]], p)
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = []
    p2 = []
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            p1.append(card[i])
            if len(p1) >= 3:
                result = False
                used = [0] * len(p1)
                recur(0, [], p1)
                if result:
                    winner = 1
                    break
        else:
            p2.append(card[i])
            if len(p2) >= 3:
                result = False
                used = [0] * len(p2)
                recur(0, [], p2)
                if result:
                    winner = 2
                    break

    print(f'#{tc} {winner}')

