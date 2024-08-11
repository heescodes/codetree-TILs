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
def can_go():
    return in_range() and not is_wall()

def get_min_dis(pos1, pos2):
    (x1,y1),(x2,y2) = pos1,pos2
    return abs(x1-x2) + abs(y1-y2)

def get_squ_info(s_exit):
    dq = deque()
    squ_info = tuple() #(sq_len,sq_pos)
    _visited = [[False]*(n) for _ in range(n)]
    x,y = s_exit
    dq.append(s_exit)

    while dq:
        for i,j in zip(dx,dy):
            nx, ny = x+i, y+j
            for px,py in players:
                if nx == px and ny == py:
                    sq_len = abs(nx-px)
        #좌표따라 sq_pos 도출방식 달라지는 로직구현

def rotate:


def do_move:

                







'''
def get_min_squ():
    

### Function ###


def rotate():


def do_move():
'''