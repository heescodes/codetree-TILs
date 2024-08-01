import sys
from collections import deque

INT_MAX = sys.maxsize

### Input ###
n, m = map(int, input().split())
arr = [[None] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i][1:] = list(map(int, input().split()))
stores = [None] + [tuple(map(int, input().split())) for _ in range(m)]
##############

### Global ###
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
player_cpos = [None] * (m + 1)
cur_t = 0
# bfs에 사용되는 변수들입니다.
# 최단거리 결과 기록
step = [
    [0]*(n+1)
    for _ in range(n+1)
]
# 방문 여부 표시
visited = [
    [False]*(n+1)
    for _ in range(n+1)
] 

ban_list = list()
done_cnt = 0
##############

### Functions ###
def is_range(pair):
    x, y = pair
    return 1 <= x <= n and 1 <= y <= n

def is_banned(pair):
    x, y = pair
    return arr[x][y] < 0

def can_go(pair):
    x,y = pair
    return is_range(pair) and not visited[x][y] and not is_banned(pair)

def move(player, pair):
    player_cpos[player] = pair
    player_visited[player][pair[0]][pair[1]] = True

def set_ban(pair):
    x, y = pair
    arr[x][y] = -1

def get_base(player):  # BFS 기본포맷 익숙해지기
    found_base = []
    dq = deque()
    for i in range(n+1):
        for j in range(n+1):
            visited[i][j] = False

    #_visited = [[False]*(n+1) for _ in range(n+1)]
    x, y = stores[player]
    dq.append((x, y))
    visited[x][y] = True
    #_visited[x][y] = True

    while dq and not found_base:
        x, y = dq.popleft()
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if can_go((nx, ny)):
                dq.append((nx, ny))
                visited[nx][ny] = True
                if arr[nx][ny] == 1:
                    found_base.append((nx, ny))
    
    found_base.sort()  # sort 세부분석하기
    return found_base[0]

def bfs(cur_pos):
    for i in range(n+1):
        for j in range(n+1):
            visited[i][j] = False
            step[i][j] = 0
    
    dq = deque()
    dq.append(cur_pos)
    sx,sy = cur_pos
    visited[sx][sy] = True
    step[sx][sy] = 0

    while dq:
        x,y = dq.popleft()
        for i,j in zip(dx,dy):
            nx,ny = x+i, y+j
            if can_go((nx,ny)) and not visited[nx][ny]:
                visited[nx][ny] = True
                #최단거리 
                dq.append((nx,ny))
                step[nx][ny] = step[x][y] + 1
    #print(f'step:{step}')

def do_action():
    ##########
    # action_1
    ##########
    for player in range(1,m+1):
        if player_cpos[player] == None or player_cpos[player] == stores[player]:
            continue

        bfs(stores[player]) #핵심 아이디어: 편의점 -> 현재위치로 bfs 왜???

        cx,cy = player_cpos[player]

        min_dist = INT_MAX
        min_x, min_y = -1, -1
        for i, j in zip(dx,dy):
            nx,ny = cx+i, cy+j
            if is_range((nx,ny)) and visited[nx][ny] and min_dist > step[nx][ny]: # 핵심아이디어: 
                min_dist = step[nx][ny]
                min_x,min_y = nx,ny
            
        player_cpos[player] = (min_x, min_y)
    
    ##########
    # action_2
    ##########
    for player in range(1,m+1):
        if player_cpos[player] == stores[player]:
            pos = player_cpos[player]
            set_ban(pos)

    ##########
    # action_3
    ##########
    if cur_t > m:
        return

    base = get_base(cur_t)    #개선포인트: bfs 재활용할 수 있을텐데 ???
    player_cpos[cur_t] = base
    #print(f'cur_t,base,cpos:{cur_t},{base},{player_cpos[cur_t]}')
    set_ban(base)


def end():
    for i in range(1,m+1):
        if player_cpos[i] != stores[i]:
            return False
    return True

#####################
# main
while True:
    cur_t += 1
    do_action()
    if end():
        break
print(cur_t)