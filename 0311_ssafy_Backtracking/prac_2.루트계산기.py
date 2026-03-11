import sys
sys.stdin = open('0311_ssafy_Backtracking/input.txt', 'r')


# def binary_search(target):
#     left = 0
#     right = target

#     while left <= right:
#         mid = (left + right) // 2

#         if target < mid*mid:
#             right = mid - 1
#         else:
#             left = mid + 1

#     return right


# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     result = n ** 0.5
#     print(f'#{tc} {binary_search(n)}')

# 1. mid 값을 본다
# 2. mid*mid이 target보다 작다 -> 오른쪽을 탐색
# 3. mid*mid가 target보다 크다 -> 왼쪽을 탐색

# 각 단계에서 mid와 target을 가지고 조건을 검사
# 조건이 True 일 때 오른쪽을 탐색하도록 구현
def check(mid, target):
    if mid*mid <= target:
        return True
    return False

def binary_search(target):
    left = 0
    right = target

    while left <= right:
        mid = (left+right) // 2

        # 2. mid*mid이 target보다 작다 -> 오른쪽을 탐색
        if check(mid, target):
            left = mid + 1

        # 3. mid*mid가 target보다 크다 -> 왼쪽을 탐색
        else:
            right = mid - 1

    return left - 1

T = int(input())
for tc in range(1, T+1):
    target = int(input())
    result = binary_search(target)
    print(f'#{tc} {result}')
