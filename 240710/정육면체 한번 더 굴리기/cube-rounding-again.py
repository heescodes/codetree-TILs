#1h20m+21:27~
from copy import deepcopy
from collections import deque

n,m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

#동,남,서,북 (시계)
dx = [+1,0,-1,0]
dy = [0,+1,0,-1]
''' <dice index>
[0]:bottom
   [5]
[3][0][1][2]
   [4]
'''   
dice = [6,3,1,4,2,5]

def dice_update(dirnum):
    tmp_dice = deepcopy(dice)
    #동
    if dirnum==0:
        dice[3] = tmp_dice[0]
        dice[0] = tmp_dice[1]
        dice[1] = tmp_dice[2]
        dice[2] = tmp_dice[3]
    #남
    if dirnum==1:
        dice[2] = tmp_dice[5]
        dice[4] = tmp_dice[2]
        dice[0] = tmp_dice[4]
        dice[5] = tmp_dice[0]
    #서
    if dirnum==2:
        dice[3] = tmp_dice[2]
        dice[0] = tmp_dice[3]
        dice[1] = tmp_dice[0]
        dice[2] = tmp_dice[1]
    #북
    if dirnum==3:
        dice[2] = tmp_dice[4]
        dice[4] = tmp_dice[0]
        dice[0] = tmp_dice[5]
        dice[5] = tmp_dice[2]

def get_direction(cx,cy,cdir):
    ndir = cdir
    if dice[0] > arr[cy][cx]:
        ndir = (cdir + 1) % 4
    if dice[0] < arr[cy][cx]:
        ndir = (cdir - 1) % 4
    return ndir     

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move_dice(x,y,dirnum):
    nx = x + dx[dirnum]
    ny = y + dy[dirnum]
    dice_update(dirnum)

    if not(in_range(nx,ny)):
        new_dirnum = dirnum+2%4
        nx = x + dx[new_dirnum]
        ny = y + dy[new_dirnum]
        dice_update(new_dirnum)
    return nx,ny 

def get_score(cx,cy):
    mynum = arr[cy][cx]
    score = mynum
    q = deque()
    visited = [[False]*n for _ in range(n)]

    q.append((cx,cy))
    visited[cy][cx] = True
    while q:
        x,y = q.popleft()
        for i,j in zip(dx,dy):
            nx,ny = x+i,y+j 
            if in_range(nx,ny) and arr[ny][nx] == mynum \
            and not(visited[ny][nx]):
                score += mynum
                q.append((nx,ny))
                visited[ny][nx] = True
    return score

direction = 0
score = 0
def simul(sx,sy):
    global direction, score
    x,y = move_dice(sx,sy,direction)
    #print(f'bot:{dice[0]}',end=" ")
    #print(f'({x},{y})',end=" ")
    score += get_score(x,y)
    #print(f'score={score}', end=" ")
    direction = get_direction(x,y,direction)
    #print(f'direction={direction}')
    return x,y
#####
x,y = 0,0
for _ in range(m):
    x,y = simul(x,y)

print(score)