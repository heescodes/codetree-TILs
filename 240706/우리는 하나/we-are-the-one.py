#15:33~
from collections import deque
from itertools import combinations

_4WAY = 4 #dirnum:0~3 = e,w,s,n
n,k,u,d = map(int, input().split())
heights = [list(map(int,input().split())) for _ in range(n)]

q = deque()
visited = [list(False for _ in range(n)) for _ in range(n)]
dx = [+1,-1,0,0]
dy = [0,0,+1,-1]

def in_range(x,y):
    return ((0<=x<=n-1) and (0<=y<=n-1))

def valid_height(x,y,nx,ny):
    return (u <= abs(heights[y][x]-heights[ny][nx]) <= d)

def move(x,y,dirnum):
    return x+dx[dirnum], y+dy[dirnum]

def bfs_count(x,y):
    q.append((x,y))
    visited[y][x] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for dirnum in range(_4WAY):
            nx, ny = move(x,y,dirnum)
            #print(f'nx,ny={nx},{ny}')
            if in_range(nx,ny) and valid_height(x,y,nx,ny) \
            and not(visited[ny][nx]):
                q.append((nx,ny))
                visited[ny][nx] = True
                cnt += 1
                #print(f'cnt:{cnt}')
    return cnt

def make_k_comb(k):
    all_points = [(x, y) for x in range(n) for y in range(n)]
    start_combs = list(combinations(all_points, k))
    return start_combs


## main ##
result = 0
#print(make_k_comb(k))
for pairs in make_k_comb(k):
    for x,y in pairs:
        result = max(result, bfs_count(x,y))
print(result)