# 재귀호출
# 끝나는 지점이 필요하다

# 1. 시작
# 2. 끝
# 3. 누적된 값

# 1. 종료코드 -> 2. 다음 재귀 호출

#0 - 10 출력
# - 0부터 시작하고 10에서 종료(10보다 커지면 종료)
# 다음 재귀 호출에는 num을 1씩 증가

# 끝까지 갔다가 돌아오기

def recur(num):
    if num > 3: #3번        #기저조건, 종료조건 -> 트리의 높이, 재귀호출 깊이
        return
    
    print(num, end = ' ') # 2번
    recur(num+1) #1번       
    recur(num+1)

# recur(0)


def recur2(num):
    if num > 3:
        return
    
    print(num, end = ' ')
    for i in range(1, 7):
        recur2(num + 1)

recur2(0)
