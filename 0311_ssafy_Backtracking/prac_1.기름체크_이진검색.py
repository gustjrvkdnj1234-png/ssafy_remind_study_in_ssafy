import sys
sys.stdin = open('0311_ssafy_Backtracking/input.txt', 'r')
# #의 상태, _의 상태

# T = int(input())
# for tc in range(1, T+1):
#     n = input().strip()

#     if '#' not in n:
#         print(f'#{tc}', '0%')
#     elif '_' not in n:
#         print(f'#{tc}', '100%')

#     else:
#         length = len(n)
#         lst = []
#         for i in n:
#             if i == '#':
#                 lst.append(i)
#         result = (len(lst) / length) * 100

#         print(f'#{tc} {int(result)}%')

#이렇게 하면 안된다.

def binary_search():
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        #arr[mid] 가 #이면 오른쪽을 탐색
        if arr[mid] == '#':
            left = mid+1
        #반대면, 왼쪽을 탐색
        else:
            right = mid-1

    return int(left*100 / len(arr))
    

T = int(input())

for tc in range(1, T+1):
    arr = input().strip()
    result = binary_search()
    print(f'{tc} {result}%')