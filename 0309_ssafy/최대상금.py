import sys
sys.stdin = open('0309_ssafy/input.txt', 'r')

# 우승자 주어진 숫자판, 2개 선택, 정해진 횟수만큼 자리 교환

#오른쪽 끝부터 1, 왼쪽으로 갈 수록 * 10

#반드시 횟수만큼 교환, 동일 위치 교환 중복 ok

#정해진 횟수만큼 교환 후, 받을 수 있는 가장 큰 금액 계산.

# 시작 : 아무것도 바꾸지 않은 현재
# 종료조건 : 교환이 끝났을 때
# 종료된 것들 중에, 제일 큰 숫자 찾기 그냥 리스트 그대로 *한 정수 만들기
# 누적, 브랜치 : 교환한다. n개의 숫자?? 교환은 C번

def recur(cnt):
    global max_val
    crr = (cnt, "".join(arr))

    if crr in visited:
        return
    
    visited.add(crr)

    #교환이 끝났을 때, 그 기준으로 최대값을 환산
    if cnt == c:
        if int("".join(arr)) > max_val:
            max_val = int("".join(arr))
        return

    #처음부터 맨마지막 전까지, 그다음부터 맨마지막까지 보면서, 위치 바꾸기
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            recur(cnt + 1)
            arr[i], arr[j] = arr[j], arr[i]


# 첫 줄은 테스트 케이스의 수이다
T = int(input())
for tc in range(1, T+1):
#최대 10개의 테스트 케이스
#숫자판 정보, 교환횟수
    n, c = map(int, input().split())
#최대 자리 6, 최대 교환 10번
# len(n) <= 6, c <= 10
    arr = list(str(n))
    visited = set()
    max_val = 0
    #숫자판 n에서 일단 c번 만큼 교환해야함

    recur(0)
    print(f'#{tc} {max_val}')

