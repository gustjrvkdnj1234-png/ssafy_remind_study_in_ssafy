# import sys
# sys.stdin = open('0310_ssafy_Greedy/input.txt', 'r')

#주사위 N개를 던져서 나올 수 있는 눈금의 모든 조합 출력(구현)

#N =3 일때 : depth = 3
#brach 6

dice = [1, 2, 3, 4, 5, 6]
N = 3
path = []
# def recur(cnt):
#     if cnt == N:
#         print(path)
#         return

#     for i in range(6):
#         path.append(dice[i])
#         recur(cnt+1)
#         path.pop()

# recur(0)

# def recur(cnt, subset, prev):
#     if cnt ==N:
#         print(subset)
#         return
    
#     for i in range(prev, 6):
#         recur(cnt+1, subset + [dice[i]], i)

# recur(0, [], 0)


##중복순열인가?
# def jo(c, s):
#     if c == N:
#         print(s)
#         return
    
#     for i in range(6):
#         jo(c+1, s+[dice[i]])

# jo(0, [])

## 중복이 없는 조합인가??
# def jo(c, s, p):
#     if c == N:
#         print(s)
#         return
    
#     for i in range(p+1, 6):
#         jo(c+1, s+[dice[i]], i) #p+i가 아니라 그냥 i인가? 그렇다면 왜?

# jo(0, [], -1)

##중복이 있는 조합인가?
def jo(c, s, p):
    if c == N:
        print(s)
        return
    
    for i in range(p, len(dice)): #왜 P+1하고 p의 차이가 있지?
        jo(c+1, s+[dice[i]], i)

jo(0, [], 0)
