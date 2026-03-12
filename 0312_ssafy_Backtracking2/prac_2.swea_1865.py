import sys
sys.stdin = open('0312_ssafy_Backtracking2/input.txt', 'r')



#전체?
#종료조건 : N
# 브랜치 또한 N
def recur(cnt, crr_per):
    global max_val

    if crr_per < max_val:
        return

    if cnt == N:
        if crr_per > max_val:
            max_val = crr_per
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = 1
        path.append(i)
        recur(cnt+1, crr_per * (work[cnt][i] / 100))
        path.pop()
        visited[i] = 0


# N명의 직원 / 할 일도 N 개
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    path = []
    visited = [0] * N
    max_val = 0
    recur(0, 1)
    print(f'#{tc} {(max_val*100):.6f}')