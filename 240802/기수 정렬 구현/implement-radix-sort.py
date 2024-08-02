arr_size= int(input())
arr= input().split()

pos= len(arr[0])
for i in range(pos-1,-1,-1):
    arr_new = [[] for i in range(10)]
    for j in arr:
        arr_new[int(j[i])].append(j)
        
    arr_store = []
    for a in arr_new:
        for b in a:
            arr_store.append(b)
    arr = arr_store

for i in arr:
    print(i,end=" ")