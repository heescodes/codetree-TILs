from collections import deque
_4WAY = 4
n,m = map(int,input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
#print(arr)

#[0]:동/[1]:서/[2]:남/[3]:북
dx = [+1, -1, 0, 0] 
dy = [0, 0, +1, -1]
q = deque()

def init_pos():
    q.append((0,0))

def is_valid(x, y):
    if 0<=x<=m-1 and 0<=y<=n-1 and not(arr[y][x]):
        return True
    else:
        return False

def mov(dirnum, x, y):
    x += dx[dirnum]
    y += dy[dirnum]
    return x, y

def is_escaped(x, y):
    if (y == n-1) and (x == m-1):
        return True
    else:
        False

def bfs():
    init_pos()
    while q:
        x, y = q.popleft()
        for i in range(_4WAY):
            nx, ny = mov(i, x, y)
            if is_valid(nx,ny):
                #print(f'nx,ny:{nx},{ny}')
                q.append((nx,ny))
            if is_escaped(nx,ny):
                return 1  
    return 0

print(bfs())