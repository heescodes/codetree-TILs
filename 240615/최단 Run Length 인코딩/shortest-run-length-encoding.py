#16:23

strs = list(input())

#종료조건
#그냥 매번RLE체크

#rshft
def rshft():
    strs.insert(0,strs.pop())

#get RLE
def get_RLE():
    res = list()
    cnt = 0
    pre_key = strs[0]
    #print(f'strs:{strs}')
    for i in range(len(strs)):
        cur_key = strs[i]
        if pre_key != cur_key:
            res.append(pre_key)
            res.append(str(cnt))
            cnt = 1
        else:    
            cnt += 1

        if i == len(strs)-1:
            res.append(pre_key)
            res.append(str(cnt))
        else:    
            pre_key = cur_key 

    res = ''.join(res)    
    return res

#main
rle = list()
res_len = 1000

for _ in range(len(strs)):
    rle = get_RLE()
    #''.join(rle)
    res_len = min(len(rle),res_len)
    rshft()

print(res_len)