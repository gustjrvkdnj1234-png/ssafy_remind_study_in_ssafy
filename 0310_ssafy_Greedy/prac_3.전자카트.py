import sys
sys.stdin = open('0310_ssafy_Greedy/input.txt', 'r')

#사무실에서 출발, 각 구역 한 번씩 방문, 사무실로 돌아옴 > 최소 배터리

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #시작과 마지막은 1로 고정 각 구역 N번까지 한 번씩만 들어갈 수 있는 경우
    #1231, 1321 2가지 경우 중복 안됌. 처음 마지막 제외 후?안쪽만 만들고, 양 끝에 1을 붙인다음 계산?

    # 5라면 12345 (2345)로 나올 수 있는, N이 5면 총6자리. 도는 건 4자리.
    # 중복 안되는 순서는 달라도 되는. 순열.
    #depth 는 N-1이면 멈추기
    #브랜치는 2부터 시작해서 N개까지. 총 N-1개 동일
    lst = [x for x in range(2, N+1)]
    used = [0] * (N+1)

    def min_cal(lst):
        total = 0
        lst1 = [1] + lst + [1]
        lst2 = []
        #1231, 1321 - 0120, 0210 / 01, 12, 20 / 02, 21, 10
        for x in lst1:
            lst2.append(x-1)
        for idx in range(len(lst2)-1): # 0 1 2 0 / 4 / 0 1 2 3
            total += arr[lst2[idx]][lst2[idx+1]]
        return total
    min_val = float("inf")

    def recur(cnt,subset):
        global min_val
        #모든 경우 구해서, 각각 마다 소비량 체크하기
        if cnt == (N-1):
            total = min_cal(subset)
            if total < min_val:
                min_val = total
            # print(*subset)
            return

        for i in range(N-1):
            if used[i] == 1:
                continue
            used[i] = 1
            recur(cnt+1, subset + [lst[i]])
            used[i] = 0

        return min_val
    
    print(f'#{tc} {recur(0, [])}')