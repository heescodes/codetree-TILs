#22:00
DBG = False

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

#dirnum 0~3 : w,s,e,n 
dx = [-1,0,+1,0]
dy = [0,+1,0,-1]
out_dust = 0
start = (n//2,n//2)
direction = 0
turn_cnt = 0

def in_range(pair):
    x,y = pair
    return 0<=x<n and 0<=y<n

def mov2curr(prev,dirnum):
    x,y = prev
    return (x+dx[dirnum],y+dy[dirnum])

#add dust & count outrange dust
def add_dust(curr,dirnum):
    global out_dust
    cx,cy = curr

    if DBG: print(f'cx,cy:{cx},{cy}')  

    add_1 = int(arr[cy][cx] * 0.01)
    add_2 = int(arr[cy][cx] * 0.02)
    add_5 = int(arr[cy][cx] * 0.05)
    add_7 = int(arr[cy][cx] * 0.07)
    add_10 = int(arr[cy][cx] * 0.1) 
    add_all = 2*(add_1+add_2+add_7+add_10) + add_5
    add_a = arr[cy][cx] - add_all

    #1%
    x_1, y_1    = cx - dx[dirnum] - dy[dirnum], cy + dx[dirnum] - dy[dirnum]
    _x_1, _y_1  = cx - dx[dirnum] + dy[dirnum], cy - dx[dirnum] - dy[dirnum]
    if in_range((x_1,y_1)):
        arr[y_1][x_1] += add_1
    else:
        out_dust += add_1
    if in_range((_x_1,_y_1)):
        arr[_y_1][_x_1] += add_1
    else:
        out_dust += add_1

    #7%
    x_7, y_7    = cx - dy[dirnum], cy + dx[dirnum]
    _x_7, _y_7  = cx + dy[dirnum], cy - dx[dirnum]
    if in_range((x_7,y_7)):
        arr[y_7][x_7] += add_7
    else:
        out_dust += add_7
    if in_range((_x_7,_y_7)):
        arr[_y_7][_x_7] += add_7
    else:
        out_dust += add_7

    #2%
    x_2, y_2    = cx - 2*dy[dirnum], cy + 2*dx[dirnum]
    _x_2, _y_2  = cx + 2*dy[dirnum], cy - 2*dx[dirnum]
    if in_range((x_2,y_2)):
        arr[y_2][x_2] += add_2
    else:
        out_dust += add_2
    if in_range((_x_2,_y_2)):
        arr[_y_2][_x_2] += add_2
    else:
        out_dust += add_2

    #10%
    x_10, y_10    = cx + dx[dirnum] - dy[dirnum], cy + dx[dirnum] + dy[dirnum]
    _x_10, _y_10 = cx + dx[dirnum] + dy[dirnum], cy - dx[dirnum] + dy[dirnum]
    if in_range((x_10,y_10)):
        arr[y_10][x_10] += add_10
    else:
        out_dust += add_10
    if in_range((_x_10,_y_10)):
        arr[_y_10][_x_10] += add_10
    else:
        out_dust += add_10

    #5%
    x_5, y_5 = cx + 2*dx[dirnum], cy + 2*dy[dirnum]
    if in_range((x_5,y_5)):
        arr[y_5][x_5] += add_5
    else:
        out_dust += add_5

    #a%
    x_a, y_a = cx + dx[dirnum], cy + dy[dirnum]
    if in_range((x_a,y_a)):
        arr[y_a][x_a] += add_a
    else:
        out_dust += add_a

    arr[cy][cx] = 0
    #if DBG: print(f'1%:({x_1},{y_1})')
    #if DBG: print(f'out_dust:{out_dust}')

def simul(pair):
    global direction
    x,y = pair
    while x!=0 and y!=0:
        for go_len in range(1, n+1):
            for _ in range(2):
                for _ in range(go_len):
                    x,y = mov2curr((x,y),direction)
                    add_dust((x,y),direction)
                    if DBG: print(f'direction:{direction}')
                    if x==0 and y==0:
                        return
                    '''
                    for row in arr: # 이차원 배열 출력
                        for elem in row:
                            print(elem, end=" ")
                        print()
                    print(f'out_dust:{out_dust}')
                    print()
                    '''
                    
                direction = (direction + 1) % 4
                

simul(start)
print(out_dust)