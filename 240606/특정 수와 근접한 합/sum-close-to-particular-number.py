N, S = map(int,input().split())
arr = [int(x) for x in input().split()]
min_gap = 10000

for i in range(N):
    for j in range(i+1, N):
        cur_sum = sum(arr) - arr[i] - arr[j]
        cur_gap = abs(S - cur_sum)

        min_gap = min(cur_gap, min_gap)

print(min_gap)