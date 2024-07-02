#1h + 21:48~
###############################################
#1년 성장과정
    #1. 영양제 이동
    #2. 이동후 영양제 투입
    #3. 투입직후 높이 +1
    #4. 대각선 인접방향에 높이1이상 개수만큼 추가성장
    #5. 영양제 투입된 나무 제외, 높이2이상은 -2하고 해당위치 영양제투입
###############################################
n,m = map(int,input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
#print(arr)
dps = list(tuple(map(int, input().split())) for _ in range(m)) 
#print(dps)

med_posses = list()
tmp = list()
direction = [(0,0),(+1,0),(+1,+1),(0,+1),(-1,+1),(-1,0),(-1,-1),(0,-1),(+1,-1)]

#영양제1 위치 저장
def save_med_pos(x,y):
    med_posses.append([x,y])

#영양제1 위치 pop
def pop_med_pos():
    if not med_posses:
        return False
    return med_posses.pop()

#영양제들 위치 초기조건(x,y)
def init_med_pos():
    save_med_pos(0,n-2)
    save_med_pos(1,n-2)
    save_med_pos(0,n-1)
    save_med_pos(1,n-1)
    return

#1. 영양제들 좌표변경
def med_mov(d, p):
    #print(f'direction[{d}]:{direction[d]}')
    dx = direction[d][0]
    dy = direction[d][1]
    movsz = p % n
    
    #for until len(med_posses)
    for pair in med_posses:
        #영양제 좌표변경
        for _ in range(movsz):
            pair[0] += dx
            pair[1] += dy
            if (pair[0] > n-1) or (pair[0] < 0):
                pair[0] = n - abs(pair[0])
            if (pair[1] > n-1) or (pair[1] < 0):
                pair[1] = n - abs(pair[1])
    #print(f'med_posses:{med_posses}')
    return

#2,3. 영양제들 투입 & 높이+1 성장
def inject_med():
    #for until len(med_posses)
    for pair in med_posses:
        #높이+1
        arr[pair[1]][pair[0]] += 1
    return

def save_grow_cnt(tmp_arr,x,y,cnt_val):
    tmp_arr[y][x] = cnt_val
    return tmp_arr

#4. 영양제들 대각선인접(2,4,6,8) 높이1이상 탐색 & 추가성장
def additional_grow():
    tmp_arr = [[0]*n for _ in range(n)]
    for pair in med_posses:
        grow_cnt = 0
        for i in range(2,9,2):
            x = pair[0]+direction[i][0]
            y = pair[1]+direction[i][1] 
            if (0 <= x <= n-1) and (0 <= y <= n-1):
                if arr[y][x] >= 1:
                    grow_cnt += 1
        #print(f'({pair[0]},{pair[1]})grow_cnt:{grow_cnt}')    
        #arr[pair[1]][pair[0]] += grow_cnt
        tmp_arr = save_grow_cnt(tmp_arr,pair[0],pair[1],grow_cnt)
        #print(f'tmp_arr:{tmp_arr}')
    for j in range(n):
        for i in range(n):
            arr[j][i] += tmp_arr[j][i]
    return

def old_med_flag(posses):
    arr = [[True]*n for _ in range(n)]
    for pair in posses:
        arr[pair[1]][pair[0]] = False
    return arr

#5. 기존 med_pos제외, 2이상 베고 해당위치로 영양제 위치 갱신
def cut_update_med_pos():
    flags = old_med_flag(med_posses)
    med_posses.clear()
    for j in range(n):
        for i in range(n):
            if flags[j][i]:
                if arr[j][i] >= 2:
                    arr[j][i] -= 2
                    save_med_pos(i,j)
    return

def print_sum_all():
    height = 0
    for j in range(n):
        for i in range(n):
            height += arr[j][i]
    print(height)
    return


## Main ##
init_med_pos()
#print(f'init:{med_posses}')
for dp in dps:
    #print(f'dp:{dp}')
    med_mov(dp[0],dp[1])
    #print(f'after med_mov:\n{arr}')
    inject_med()
    additional_grow()
    #print(f'after additional_grow:\n{arr}')
    cut_update_med_pos()
    #print(f'after cut_update_med_pos:\n{arr}')
    #print(f'med_posses:{med_posses}')
print_sum_all()