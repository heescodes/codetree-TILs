#11:59~#13:00
 
from collections import deque
 
### Input ###
n,m,k = tuple(map(int,input().split()))
maze = [list(map(int, input().split())) for _ in range(n)]
players = [tuple(map(int, input().split())) for _ in range(m)]
 
### Global ###
dx = (0,0,-1,+1)
dy = (-1,+1,0,0)
 
 
### API ###
def in_range(pos):
    return 0<=pos[0]-1<=n and 0<=pos[1]-1<=n
def is_wall(pos):
    return 1 <= maze[pos[0]-1][pos[1]-1] <= 9
def can_go(pos):
    return in_range(pos) and not is_wall(pos)
 
def get_min_dis(pos1, pos2):
    (x1,y1),(x2,y2) = pos1,pos2
    return abs(x1-x2) + abs(y1-y2)
 
def get_squ_pos(pos1, pos2, squ_len):
    pos = None
    (x1,y1),(x2,y2) = pos1,pos2

    if x1 != x2 and y1 == y2:
        x, y = min(x1,x2), y1
        for j in range(squ_len+1) :
            y = y1 - j
            if in_range((x,y)) and j < squ_len:
                pos = (x,y)
            else:
                return pos
    if x1 == x2 and y1 != y2:
        x, y = x1, min(y1, y2)
        for i in range(squ_len+1):
            x = x1 - i
            if in_range((x,y)):
                pos = (x,y)
            else:
                return pos
    if x1 != x2 and y1 != y2:
        pos = (min(x1, x2), min(y1, y2))
        return pos


def get_squ_info(s_exit):
    dq = deque()
    squ_info = list()
    _visited = [[False]*(n) for _ in range(n)]
    x,y = s_exit
    dq.append(s_exit)
 
    while dq:
        for i,j in zip(dx,dy):
            nx, ny = x+i, y+j
            for px,py in players:
                if nx == px and ny == py:
                    sq_len = abs(nx-px)
                    sq_pos = get_squ_pos((nx,ny),(px,py),sq_len)
                    squ_info.append((sq_len, sq_pos))
                    
        
        #좌표따라 sq_pos 도출방식 달라지는 로직구현
'''
def rotate:
 
 
def do_move:
'''
                
 
 
 
 
 
 
 
'''
def get_min_squ():

n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
players = [tuple(map(int, input().split())) for _ in range(m)]
exit = tuple(map(int, input().split()))

dr = [-1, +1, 0, 0]
dc = [0, 0, -1, +1]
visited = [[False]*(n) for _ in range(n)]

def in_range(r,c):
    return 1<=r<=n and 1<=c<=n

def is_wall(r,c):
    return 1<=maze[r-1][c-1]<=9

def can_mov(r,c):
    return in_range(r,c) and not(is_wall(r,c))

def min_distance(pair1, pair2):
    x1,y1 = pair1
    x2,y2 = pair2
    return abs(x1-x2) + abs(y1-y2)

#최소 정사각형 도출
def get_min_square():
    for player in range(1, m+1):
        dq = deque()
        min_exit = []
        min_len = 10 
        x,y = players[player-1]
        dq.append((x,y))
        visited[x-1][y-1] = True
        while dq and not(min_exit):
            x, y = dq.popleft()
            for dx, dy in zip(dr,dc):
                nx, xy = x+dx, y+dy
                if maze[nx-1][ny-1] == exit[player-1]:
                    min_exit.append((nx,ny))
                dq.append((nx,ny))
                visited[nx-1][ny-1] = True
            
        #player위치, min_exit로부터 최소 squ 도출(entry,len)


def move():


def minus_dura():

#부분회전 
def rotate():
    #rotate


    #minus_dura()
'''