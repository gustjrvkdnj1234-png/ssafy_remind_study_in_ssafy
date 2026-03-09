
#0이상 9이하의 번호가 적힌 6장의 카드

#3장의 카드가 연속적인 번호를 갖는 경우 run 이라고 함
#3장의 카드가 동일 번호 triplet

# 6장의 카드가 run과 triplet 으로만 구성되면 baby-gin

#6장의 입력 > depth
#branch?

#3장 카드가 연속번호인가? 3장이 연속되는가를 어떻게?
#3장의 카드가 동일한가? > 동일하면 3장 제거
# visited = [0] * 6
# card = list(map(int,input().split()))

# def baby():
#     for i in (0, 3):
#         #연속되는가를 어떻게 찾지?
#         if path[i] + 1 == path[i+1] and path[i+1] + 1 == path[i+2]: return True
#         if path[i] == path[i+1] and path[i+1] == path[i+2]: return True
#         return False

# path = []
# def gin(card):
#     if len(path) == 6:
#         print(*path)
#         return
    
#     for i in range(len(card)):
#         visited[i] = True # 0 1 2 3 4 5
#         path.append(i)
#         gin(card[:i+1])
#         path.pop()

# gin(card)

##---------------------------------------------------##

#다 줄을 세워보자.

# 1. 전체 순열을 만든다.
# 2. 문제 추가 조건을 구현한다.

import sys
sys.stdin = open('0309_ssafy/input.txt', 'r')

path = []
used = [0] * 6
result = False

#- 시작점은 6개의 카드를 모두 고려, 줄 세우기
# 종료조건: 6개의 카드를 모두 줄 세우면 종료(depth = 6)
# 재귀호출 : 6개의 카드(branch = 6)

def is_baby_gin():
    cnt = 0

    #앞의 3개 숫자
    # - run + tri 비교
    # 동일
    a, b, c = path[0], path[1], path[2]
    if a == b == c:
        cnt+= 1
    elif a == (b-1) == (c-2):
        cnt += 1
    #뒤에 3개 숫자
    a, b, c = path[3], path[4], path[5]
    if a == b == c:
        cnt+= 1
    elif a == (b-1) == (c-2):
        cnt += 1
    
    return cnt == 2

def recur(cnt):
    global result
    if cnt == 6:
        # print(*path)
        if is_baby_gin():
            result = True
        return
    
    for i in range(6):
        if used[i]:
            continue

        used[i] = 1
        path.append(arr[i])
        recur(cnt + 1)
        path.pop()
        used[i] = 0


arr = list(map(int, input().split()))
recur(0)

print(result)



## input 예시
# 6 6 7 7 6 7
# 0 5 4 0 6 0
# 1 0 1 1 2 3