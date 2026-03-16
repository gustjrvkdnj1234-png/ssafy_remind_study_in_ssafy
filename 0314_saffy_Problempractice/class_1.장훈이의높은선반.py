def recur(cnt, current_sum):
    global min_val
 
    if current_sum >= min_val:
        return
     
    if current_sum >= S:
        if current_sum < min_val:
            min_val = current_sum
        return
 
    if cnt == N:
        return
     
    #현재 값을 같이 넣는다.
    recur(cnt +1, current_sum + tall[cnt])
 
    #현재 값 포함하지 않고 간다.
    recur(cnt +1, current_sum)
 
T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    tall = list(map(int, input().split()))
 
    path = []
    visited = [0] * N
    min_val = float("inf")
    recur(0,0)
    print(f'#{tc} {abs(S - min_val)}')