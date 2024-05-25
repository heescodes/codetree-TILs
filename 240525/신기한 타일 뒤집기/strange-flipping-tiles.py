#14:07~14:46

tiles = [0 for _ in range(200001)]
cur_idx = 100000

def filp_tile(x, movdir):
    global cur_idx
    if movdir=="R": #Black
        for i in range(cur_idx, cur_idx+x, 1):
            tiles[i] = 1
            cur_idx=i
    if movdir=="L": #White
        for i in range(cur_idx, cur_idx-x, -1):
            tiles[i] = -1
            cur_idx=i
    #print(f"cur_idx: {cur_idx}")
    #print(tiles[90:111:1])

n = int(input())
for _ in range(n):
    x, movdir = input().split()
    filp_tile(int(x), movdir)

print("%d %d" % (tiles.count(-1), tiles.count(1)))