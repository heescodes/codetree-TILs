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

def rotate(squ_info):
    N = squ_info[0]
    tmp = [[None]*(N) for _ in range(N)]
    x_off, y_off = squ_info[1]

    for r in range(N):
        for c in range(N):
            print(f"---({N-(r-1)-1},{x_off + c-1})")
            print(maze[(x_off + c-1)][N-(y_off + r-1)+1])
            #print(maze[y_off + r-1][x_off + c-1])
            #tmp[x_off + c-1][N-(y_off + r-1)+1] = maze[y_off + r-1][x_off + c-1]
    
    print(tmp)

rotate((3,(1,1)))
 
#def do_move: