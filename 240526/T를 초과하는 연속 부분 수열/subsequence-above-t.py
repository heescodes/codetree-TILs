#17:37

n, t = map(int,input().split())
arr = [int(x) for x in input().split()]
START = 0
END = 0
seqcnt = 1

def cal_seqcnt(t):
    global seqcnt, START, END
    tmpcnt = 1
    for i in range(START, len(arr)-1):
        END = i
        if arr[idx+1] > t:
            tmpcnt += 1
            #print(f'tmpcnt: {tmpcnt}')
        else:
            #END = i
            break
            #print(f'i: {i}')
    seqcnt = max(tmpcnt, seqcnt)
    

idx = 0
while(idx < len(arr)-1):
    if arr[idx] > t:
        START = idx
        #print(f'START:{START}')
        cal_seqcnt(t)
        #print(f'END:{END}')
        idx = END+1
    else:
        idx += 1
    print('------------')

'''
def cal_seqcnt(start):
    global seqcnt, START, END
    tmpcnt = 1
    for i in range(START, len(arr)-1):
        END = i+1
        if arr[i]+1 == arr[i+1]:
            tmpcnt += 1
            #print(f'tmpcnt: {tmpcnt}')
        else:
            break
            #print(f'i: {i}')
    seqcnt = max(tmpcnt, seqcnt)
    

idx = 0
while(idx < len(arr)-1):
    #print(f'idx:{idx}')
    if arr[idx] > t:
        START = idx
        #print(f'START:{START}')
        cal_seqcnt(START)
        #print(f'END:{END}')
        idx = END
    else:
        idx += 1
    #print('------------')
'''


if seqcnt == 1:
    print(0)
elif seqcnt > 1:
    print(seqcnt)