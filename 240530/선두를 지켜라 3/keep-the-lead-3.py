#21:00
A=[]
B=[]
VEL=0
TIME=1
total_time = 0

def save_input(n, m):
    global total_time
    for _ in range(N):
        av, at = map(int, input().split())
        A.append((av, at))
        total_time += at
    for _ in range(M):
        bv, bt = map(int, input().split())
        B.append((bv, bt))

def count_honor_comb():
    comb_state = 'NONE'  # 'A','B','BOTH' 
    dasum,dbsum,acnt,bcnt = 0,0,0,0
    tcnt, tacnt, tbcnt = 1,1,1
    result = 0
    while tcnt <= total_time:
        dasum += A[acnt][VEL]
        dbsum += B[bcnt][VEL]
        #print(f'({tcnt})dasum:dbsum = {dasum}:{dbsum})')
        if dasum > dbsum:
            tmp_state = 'A'
        elif dasum < dbsum:
            tmp_state = 'B'
        else:
            tmp_state = 'BOTH'
        #print(f'({tcnt})comb_state:{comb_state}')
        if comb_state != tmp_state:
            comb_state = tmp_state
            result += 1

        if tacnt == A[acnt][TIME]:
            acnt += 1
            tacnt = 0
        if tbcnt == B[bcnt][TIME]:
            bcnt += 1
            tbcnt = 0
        tcnt += 1
        tacnt += 1
        tbcnt += 1
    print(result)

############################################
N, M = map(int, input().split())

save_input(N, M)
count_honor_comb()