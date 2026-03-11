#1. 분할 정복

# 정렬
# 1. 한 단계씩 과정 그려보기 (원리 이해)
# 2. 복잡도
# 3. 코드

# 한 번에 정답이 안나와서 작게 쪼개자. > 분할될 수 없을 때까지?

# 병합 정렬

# 퀵 정렬
    # 기준아이템 중심, 작은 것을 왼쪽, 큰것을 오른쪽

# 1. 병합 / 퀵 정렬
# - 그림 그려보기

# 2. 이진 검색
# - 기본 이진 검색
# - lower bound, upper bound
# - parametric search

graph = [[] for _ in range(7)]
u, v, w = 1, 4, 2
graph[u].append((v, w))
graph[1].append((7,8))
print(graph)