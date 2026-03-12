import sys
sys.stdin = open('0312_ssafy_Backtracking2/input.txt', 'r')

import heapq
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]

    for _ in range(M):
        start, end, time = map(int, input().split()) 
        #시작지에서 도착지까지 비용은 time

        #인접 리스트 만들기
        adj[start].append((end, time))

    #최단 거리 담을 곳
    dist = [float("inf")] * N
    dist[0] = 0

    pq = []
    heapq.heappush(pq, (0,0))   # 비용 0, 0번 노드
    
    while pq:
        #비용d, 내가 지금 도착한 역 번호 // 0번역에 0원 들여서 도착
        d, now = heapq.heappop(pq)
        if dist[now] < d:
            continue

        for next_node, fare in adj[now]:
            cost = d + fare #새로운 총 비용

            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    ans = dist[N-1]
    if ans == float("inf"):
        print(f'#{tc} impossible')
    else:
        print(f'#{tc} {ans}')
    
