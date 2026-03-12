import sys
sys.stdin = open('0313_ssafy_Problempractice/input.txt', 'r')

#A, B, C
# A < B < C
# 숫자 세 개를 받는다.
# 첫번째 수는 B보다 작아야하면서 B또한 C보다 작아야한다.

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    a1, a2, a3 = A, B, C

    if a2 >= a3:
        a2 = a3-1
    if a1 >= a2:
        a1 = a2-1

    if a1 < 1 or a2 < 1:
        print(f'#{tc}', -1)
    
    else:
        cnt = (A - a1) + (B - a2)
        print(f'#{tc} {cnt}')
        
    
# A B C 
# B = C-1 이 될 때까지 빼라.
# 원래 B에서 마지막 B 빼기
# A = B-1 이 될 때까지 빼라.
# A도 동일
# 1 100 3
# 틀림.

