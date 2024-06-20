#22:18
TIME=0
PROFIT=1
n = int(input())
tp = [tuple(map(int, input().split())) for _ in range(n)]

#작업 시작날짜
def start_date(worknum):
    return worknum

#작업 종료날짜
def end_date(worknum):
    return worknum - 1 + tp[worknum-1][TIME]

def get_profit(worknum):
    return tp[worknum-1][PROFIT]

#작업1,2

#cur_work = 1
#nxt_work = 2
total_profit = 0
result = 0


def dfs(cur_work, nxt_work):
    global total_profit

    if n == 1:
        if end_date(cur_work) <= n:
            total_profit = get_profit(cur_work)
        return

    if cur_work == n-1:
        if end_date(cur_work) == start_date(nxt_work):
            total_profit += get_profit(cur_work)
        elif end_date(cur_work) < start_date(nxt_work) and end_date(nxt_work) == n:
            total_profit += get_profit(cur_work) + get_profit(nxt_work)
        return

    if end_date(cur_work) < start_date(nxt_work): #다음작업실행가능
        total_profit += get_profit(cur_work)
        cur_work = nxt_work

    dfs(cur_work, nxt_work+1)
    return

for i in range(1, n):
    dfs(i, i+1)
    result = max(total_profit, result)

print(result)