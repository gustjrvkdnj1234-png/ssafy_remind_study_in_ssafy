#방문한 곳은 들어가지 말자.
#현재 위치에서 상하좌우를 볼 거다.


#전체 2차원 행렬을 본다.

#해당 위치가 1이고, 방문을 안 했어?
#그러면 횟수 올리고 1 추가, 방문처리, 해당 좌표 큐에 넣는다.

#큐가 있으면 계속 반복한다.
# 해당 좌표 하나 맨 앞에 위치 뺀다.
# 그리고 area??추가??
# 4방향 다 볼 거야. 해당 좌표에서,
# 혹시나 1이 있고 방문 안했다?? 그럼 방문처리하고 큐에 넣어.
#가장 많이 방문 가능한 area 내놔.





#그림은 1로 연결된 것들이 그림이다. 가로 세로로만.

#그림의 개수, 가장 넓은 그림


#위치가 1인데, 방문을 안했다 이곳. 이곳으로부터 가 궁금하니까. 이곳을 큐에 던져준다.
import sys
sys.stdin = open('0313_ssafy_Problempractice/input.txt', 'r')

from collections import deque

def bfs():
    global cnt, max_area
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1 and not visited[y][x]:
                cnt += 1
                visited[y][x] = 1
                queue = deque([(y, x)])
                area = 0

        
                while queue:
                    
                    cy, cx = queue.popleft()
                    area += 1

                    for i in range(4):
                        ny, nx = cy + dy[i], cx + dx[i]

                        if 0 > ny or ny >= N or 0 > nx or nx >= M:
                            continue

                        if arr[ny][nx] == 1 and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            queue.append((ny,nx))

                max_area = max(area, max_area)


N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dy = [1,-1,0,0]
dx = [0,0,-1,1]
cnt = 0
max_area = 0
bfs()
print(cnt)
print(max_area)