card = ['A', 'J', 'Q', 'K']

#네 종류의 카드들이 충분히 있음
# 5장의카드를 뽑아 나열
#중복 허용

#같은 종류 카드가 세 장 연속으로 나오는 경우의 수

#종료 : 5장 뽑았을 때 멈춰라
#브랜치 : 같은 종류가 세 장일 때 구하는거
#같은 종류가 3개?

path = []
result = 0
n = 3
# 012
# 123
# 234

def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

def flash(cnt):
    global result
    if cnt == 5:   #같은 게 연속되었는가 3장이 연속인가?
        if count_three():
            print(*path)
            result += 1
        return

    for i in range(4):
        path.append(card[i])
        flash(cnt + 1)
        path.pop()

flash(0)
print(result)