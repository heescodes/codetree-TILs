N, T = map(int, input().split())
cmds = input()

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir_cnt = 0
xpos, ypos = N//2, N//2
result = arr[ypos][xpos]

for direct in cmds:
    #print(f'ypos,xpos: {ypos},{xpos}')
    if direct == 'R':
        dir_cnt += 1
    elif direct == 'L':
        dir_cnt -= 1
    elif direct == 'F':
        ynxt = ypos-(dy[dir_cnt%4])
        xnxt = xpos+(dx[dir_cnt%4])
        if 0<=xnxt<N and 0<=ynxt<N:
            #print(arr[ynxt][xnxt])
            result += arr[ynxt][xnxt]
            xpos = xnxt
            ypos = ynxt
    #print(f'direct,dir_cnt: {direct},{dir_cnt}')
    #print("--------------------")
print(result)

0,1
1,1