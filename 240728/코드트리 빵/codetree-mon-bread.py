from collections import deque

### Input ###
n, m = map(int, input().split())
arr = [[None] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i][1:] = list(map(int, input().split()))
stores = [None] + [tuple(map(int, input().split())) for _ in range(m)]
##############

### Global ###
dx = [0, -1, +1, 0]
dy = [-1, 0, 0, +1]
player_cpos = [None] * (m + 1)
player_visited = [None] + [list([False] * (n + 1) for _ in range(n + 1)) for _ in range(m)]
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
    return is_range(pair) and not is_banned(pair)

def move(player, pair):
    player_cpos[player] = pair
    player_visited[player][pair[0]][pair[1]] = True

def set_ban(pair):
    x, y = pair
    arr[x][y] = -1

def get_base(player):  # BFS 기본포맷 익숙해지기
    found_base = []
    dq = deque()
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    x, y = stores[player]
    dq.append((x, y))
    visited[x][y] = True

    while dq and not found_base:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                if can_go((nx, ny)) and not visited[nx][ny]:
                    dq.append((nx, ny))
                    visited[nx][ny] = True
                    if arr[nx][ny] == 1:
                        found_base.append((nx, ny))
    
    found_base.sort()  # sort 세부분석하기
    return found_base[0]

def get_min_path(player, cpos):
    min_path = deque()
    dq = deque()
    x, y = cpos
    
    dq.append(cpos)
    visited = [[False] * (n + 1) for _ in range(n + 1)]  # BFS용 visited 배열
    visited[x][y] = True
    parent = {(x, y): None}

    while dq:
        x, y = dq.popleft()
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if cpos == (2, 2):
                print(f'{nx, ny}의 visit여부: {visited[nx][ny]}')
            if can_go((nx, ny)) and not visited[nx][ny]:
                dq.append((nx, ny))
                visited[nx][ny] = True
                parent[(nx, ny)] = (x, y)

                if (nx, ny) == stores[player]:
                    print(f'(x, y), (nx, ny): {(x, y)}, {(nx, ny)}')
                    pair = (nx, ny)
                    while pair is not None:
                        min_path.appendleft(pair)
                        pair = parent[pair]
                    return min_path
    return None

def save_ban_list(pair):
    ban_list.append(pair)

def do_ban():
    while ban_list:
        set_ban(ban_list.pop())

def do_action(player, t):
    global done_cnt
    nxt_pos = None
    # action_1
    cur_pos = player_cpos[player]
    print(f'cur_pos: {cur_pos}')
    if cur_pos and cur_pos != stores[player]:
        min_path = get_min_path(player, cur_pos)
        print(f'min_path: {min_path}')
        if min_path and len(min_path) > 0:
            nxt_pos = min_path.popleft()
            print(f'nxt_pos: {nxt_pos}')
            if nxt_pos:
                move(player, nxt_pos)
    print(f'player, player_cpos[{player}] = {player}, {player_cpos[player]}')

    # action_2
    if player_cpos[player] == stores[player]:
        x, y = player_cpos[player]
        if not player_visited[player][x][y]:
            player_visited[player][x][y] = True
            save_ban_list((x, y))
            done_cnt += 1

    # action_3
    if t == player and t <= m:
        x, y = get_base(player)
        player_cpos[player] = (x, y)
        print(f'player, base, player_cpos[{player}] = {player}, {(x, y)}, {player_cpos[player]}')
        player_visited[player][x][y] = True
        save_ban_list((x, y))
#################

### main ###
time = 1
while done_cnt < m:
    print(f'----------time: {time}----------')
    for player in range(1, m + 1):
        print(f'done_cnt = {done_cnt}')
        do_action(player, time)
    do_ban()
    time += 1

print(time)