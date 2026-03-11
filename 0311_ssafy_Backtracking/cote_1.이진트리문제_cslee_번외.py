# 결과를 저장할 장소 (이미 계산한 걸 또 하지 않기 위해)
memo = {}

def count_trees(n, k):
    """노드 n개로 높이 k '이하'인 트리를 만드는 경우의 수"""
    # 1. 기저 조건 (더 이상 나눌 수 없을 때)
    if n == 0: return 1  # 노드가 없으면 빈 트리 1가지
    if k == 0: return 0  # 높이가 0인데 노드가 있으면 불가능(0가지)
    
    # 2. 이미 계산한 적 있다면 바로 반환
    if (n, k) in memo:
        return memo[(n, k)]
    
    total = 0
    # 3. 루트 1개를 제외한 (n-1)개를 왼쪽(i)과 오른쪽(n-1-i)에 배분
    for i in range(n):
        left_ways = count_trees(i, k - 1)      # 왼쪽이 k-1 이하인 경우
        right_ways = count_trees(n - 1 - i, k - 1) # 오른쪽이 k-1 이하인 경우
        
        # 왼쪽 경우의 수 * 오른쪽 경우의 수를 모두 더함
        total += left_ways * right_ways
        
    memo[(n, k)] = total
    return total

# 실행 부분
n_input = 5
k_input = 3

# (높이 3 이하) - (높이 2 이하) = 정확히 높이 3
ans = count_trees(n_input, k_input) - count_trees(n_input, k_input - 1)
print(f"노드 {n_input}개, 높이 {k_input}인 이진트리 개수: {ans}")