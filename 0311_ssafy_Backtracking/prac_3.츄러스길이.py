import sys
sys.stdin = open('0311_ssafy_Backtracking/input.txt', 'r')

# target은 츄러스 길이 / mid
# K개

# def func(mid, target):
#     pass



# def binary_search(target):
#     left = 0
#     right = target

#     while left <= right:
#         mid = (left + right) // 2

#         if target < mid:
#             right - 1

#         else:
#             left + 1
    
#     return left

# T = int(input())
# for tc in range(1, T+1):
#     n, k = map(int, input())
#     for i in range(n):
#         churros = int(input())

#     print(f'{tc} {}')



# --------------------------------- 모범

#구하고자 하는 target - 츄러스의 길이
# - left, right, mid 가 츄러스의 길이를 의미한다는 뜻
# -> mid의 길이로 k개를 만들 수 있는가?
# - k개 이상 자를 수 있으면 더 길게, 더 긴 길이를 탐색
# - k 개를 못 만든다면 더 짧은 길이를 탐색


def test(mid):
    cnt = 0

    for churo in churros:
        cnt += churo // mid

        if cnt >= k:        #k개 이상 츄러스를 만들 수 있다
            return True
    
    return False

def binary_search():
    left, right = 1, max(churros)   #츄러스 길이의 범위

    while left <= right:
        mid = (left + right) // 2

        if test(mid):
            left = mid + 1      # mid 길이로 k개를 자를 수 있는가?
        else:                   # 있다면 더 긴 길이 탐색
            right = mid - 1            #없다면 짧은 길이 탐색

    return left - 1

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    churros = [int(input()) for _ in range(n)]
    result = binary_search()
    print(f'#{tc} {result}')