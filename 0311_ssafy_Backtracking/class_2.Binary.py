arr = [7,4,2,9,11,23,19]

# [주의!] 이진 검색은 항상 정렬된 데이터에 적용
arr.sort()

def binary_search_while(target):
    left = 0                #검색 시작점
    right = len(arr) - 1    #검색 끝점

    while left <= right:    #교차가 되는 순간이 탐색 못한 순간
        mid = (left + right) // 2

        #정답을 찾으면 종료
        if arr[mid] == target:
            return mid
        
        # arr[mid] 가 target 보다 더 큰 경우 (target이 왼쪽에 위치)
        # - 왼쪽을 탐색
        if target < arr[mid]:
            right = mid -1
        #arr[mid]가 target 보다 더 작은 경우 (target이 오른쪽에 위치)
        # - 오른쪽을 탐색
        else:
            left = mid + 1

    return -1

targets = [9, 2, 20]

for target in targets:
    result = binary_search_while(target)
    if result == -1:
        print(f'{target}은 배열에 없습니다')
    else:
        print(f'{target}은 {result}위치에 있습니다.')

print(f'9 = {binary_search_while(9)}번째 위치')
print(f'2 = {binary_search_while(2)}번째 위치')
print(f'20 = {binary_search_while(20)}번째 위치')