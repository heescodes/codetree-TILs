n = int(input())
arr = list(int(nums) for nums in input().split())

result = n


# idx : 0~n-1

def jump(idx, jcnt):
    global result
    #exit condition
    if idx == n-1:
        result = min(result, jcnt)
        return result
    elif idx > n-1 or arr[idx] == 0:
        return -1    

    #normal
    for mov in range(1, arr[idx]+1):
        idx += mov
        jcnt += 1
        jump(idx, jcnt)
        idx -= mov
        jcnt -= 1
    return

jump(0,0)

print(result)