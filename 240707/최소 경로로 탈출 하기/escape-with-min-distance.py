from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = n*m
visited = list([False]*m for _ in range(n))
q = deque()
dx = [+1,-1,0,0]
dy = [0,0,+1,-1]

def in_range(x,y):
    return 0<=x<=m-1 and 0<=y<=n-1

def is_snake(x,y):
    return arr[y][x]==0

def is_arrived(x,y):
    return (x == m-1) and (y == n-1)

def move(dirnum,x,y):
    nx = x+dx[dirnum]
    ny = y+dy[dirnum]
    return nx,ny

def get_minlen(sx,sy):
    lcnt=0
    q.append((sx,sy))
    visited[sy][sx] = True
    while q:
        x, y = q.popleft()
        if is_arrived(x,y):
            return lcnt

        for i in range(4):
            nx, ny = move(i,x,y)
            if in_range(nx,ny) and not(is_snake(nx,ny)) and not(visited[ny][nx]):
                q.append((nx,ny))
                visited[ny][nx] = True
                lcnt += 1
                print(f'nx,ny=({nx},{ny})')
                print(f'lcnt={lcnt}')
                
    return -1

print(get_minlen(0,0))