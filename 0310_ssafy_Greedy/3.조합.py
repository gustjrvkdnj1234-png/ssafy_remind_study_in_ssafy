
#이게 씨에스리 코테 완전트리일 경우 노드 경우의 수 구하기 내가 원했던 거구나.

#중복이 없는 버전
# 5명 중 N명을 뽑을 것이다
arr = ['A', 'B', 'C', 'D', 'E']

N = 3
path = []

#depth = N을 뽑으니 N
#5명 중 하나를 선택 -> branch : 5

# 1. 전체의 순열 코드부터 시작
# 2. 직전 선택을 다음 재귀호출로 넘겨준다.
# 3. 그 다음부터 선택하도록 구성

def recur(cnt, prev):
    if cnt == N:
        print(*path)
        return

    #(중복제거된 조합:)이전에 선택했던 거 다음 거부터 탐색하자!
    for i in range(prev+1, len(arr)):
        path.append(arr[i])
        recur(cnt+1, i)
        path.pop()

recur(0, -1)

#중복이 있는 버전은 어떻게???
    # prev에 +1 이 아닌 그냥 prev로 시작
    # for i in range(prev, len(arr)):
    #     path.append(arr[i])
    #     recur(cnt+1, i)
    #     path.pop()
    # recur(0, 0) <- -1이면 안됌 < 중복 허용