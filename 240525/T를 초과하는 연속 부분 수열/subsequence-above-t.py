#17:37

n, t = map(int,input().split())
arr = [int(x) for x in input().split()]
START = 0
END = 0
seqcnt = 1

#print(f'len(arr): %d',len(arr))

def cal_seqcnt(start):
    global seqcnt, START, END
    tmpcnt = 1
    for i in range(START, len(arr)-1):
        if arr[i]+1 == arr[i+1]:
            tmpcnt += 1
            #print(f'tmpcnt: {tmpcnt}')
            END = i+1
        else:
            #print(f'i: {i}')
            END = i+1
            break
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

if seqcnt == 1:
    print(0)
elif seqcnt > 1:
    print(seqcnt)