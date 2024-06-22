n = int(input())
arr = list(int(nums) for nums in input().split())

result = n+1


# idx : 0~n-1

def jump(idx, jcnt):
    global result
    #exit condition
    if idx == n-1:
        result = min(result, jcnt)
        #print(f'---idx,jcnt,result = {idx},{jcnt},{result}')
        return 0
    elif idx > n-1 or arr[idx] == 0:
        return -1    

    #normal
    for mov in range(1, arr[idx]+1):
        #print(f'idx,jcnt,result = {idx},{jcnt},{result}')
        idx += mov
        jcnt += 1
        jump(idx, jcnt)
        idx -= mov
        jcnt -= 1

    return -1

jump(0,0)
if result == n+1:
    print(-1)
else:
    print(result)