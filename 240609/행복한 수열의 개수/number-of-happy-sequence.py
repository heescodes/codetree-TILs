#02:55
ROW = 1
COL = 2
n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def is_happy(n,idx,flag):
    pre_key = 0
    for i in range(n):
        if flag == ROW:
            cur_key = arr[idx][i]
        if flag == COL:
            cur_key = arr[i][idx]
        if pre_key != cur_key:
            cnt = 0
        cnt += 1    
        pre_key = cur_key
        if cnt >= m:
            return True
    return False

def count_happys(n):
    rcnt, ccnt = 0,0
    for i in range(n):
        if is_happy(n,i,ROW) == True:
            rcnt += 1
        if is_happy(n,i,COL) == True:
            ccnt += 1
    return rcnt + ccnt

print(count_happys(n))