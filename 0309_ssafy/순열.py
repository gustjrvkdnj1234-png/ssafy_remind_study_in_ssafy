#그림은 뎁스, 가지가 몇 개인가
#[0, 1, 2] 3개의 카드가 존재
# 카드 3장 중 2장을 뽑아, 중복순열 나열 
# 1번 선택, 2번선택. -> 트리의 깊이

#기저조건: 2개의 카드를 모두 뽑았을 경우
#시작: 0개의 카드부터 시작
#다음 재귀 카드 3개 중 하나 선택

path = []
def double(cnt):
    if cnt == 2:
        print(path)
        return
    #0을 선택
    # path.append(0)
    # double(cnt + 1)
    # path.pop()
    # #1을 선택
    # path.append(1)
    # double(cnt+1)
    # path.pop()
    # #2를 선택
    # path.append(2)
    # double(cnt+1)
    # path.pop()

    #한번의 선택에 세 가지 경우의 수
    for i in range(3):
        path.append(i)  #해당 숫자를 경로에 추가
        double(cnt+1)
        path.pop()  #숫자를 뽑은 적이 없도록 초기화

# double(0)

#경로를 전역변수 쓰지 않고 하는 방법

def recur(cnt, p):
    if cnt == 2:
        print(*p)
        return
    
    for i in range(3):
        recur(cnt+1, p+[i])



# recur(0, [])

#중복은 어떻게 안 하는 가?

def recur2(cnt):
    if cnt ==3:
        print(path)
        return

    for i in range(3):
        #[주의!!!!] 너무 느리다.
        if i in path:   #시간복잡도 O(N), 전체 케이스를 다 보는 건 피해라.
            continue

    path.append(i)
    recur2(cnt+1)
    path.pop()
# recur2(0)

#중복 없애기

path = []
N = 3
used = [0] * N #N개의 종류가 있을 경우 N개 만큼

def recur3(cnt):
    if cnt ==2:
        print(*path)
        return
    
    for i in range(3):
        if used[i]:
            continue

        used[i] = 1
        path.append(i)
        recur3(cnt+1)
        path.pop()
        used[i] = 0

# recur3(0)

#주사위 3개를 던져서 합이 10 이하인 케이스의 수
#depth 는 3, branch : 6
#브랜치부터 구현한다.
# result = 0
# path = []

# def dice(cnt):
#     global result
#     if cnt ==3:
#         if sum(path) <= 10:
#             # print(*path)
#             result += 1
#         return

#     for i in range(1, 7):
#         path.append(i)
#         dice(cnt+1)
#         path.pop()        
        

# dice(0)
# print(result)


#해당 코드를 효율적으로 만든다.
# 1. 이미 10을 넘은 경우
# 2. 누적값을 파라미터로 ? 주사위의 합
result = 0
path = []

def dice(cnt, total):
    global result

    if total > 10:
        return

    if cnt ==3:
        if total <= 10:
            result += 1
        return

    for i in range(1, 7):
        dice(cnt+1, total + i)

# dice(0, 0)
# print(result)