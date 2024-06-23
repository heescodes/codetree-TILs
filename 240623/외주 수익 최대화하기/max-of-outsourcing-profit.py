#22:18
TIME=0
PROFIT=1
MAX_VAL = 99999
n = int(input())
tp = [tuple(map(int, input().split())) for _ in range(n)]

res_profit = 0
result = MAX_VAL

def update_res(curwork,prework):
    global res_profit, result
    if curwork > n+1:
        res_profit -= get_profit(prework)
    result = min(res_profit,result)
    #print(res_profit)
    return

#작업 시작날짜
def start_date(worknum):
    return worknum

#작업 종료날짜
def end_date(worknum):
    return worknum - 1 + tp[worknum-1][TIME]

def get_profit(worknum):
    return tp[worknum-1][PROFIT]

def do_work(curwork, prework):
    global res_profit
    #exit cond
    if curwork >= n+1:
        update_res(curwork, prework)
        return
    #normal
    for work in tp:
        res_profit += get_profit(curwork)
        do_work(curwork + work[TIME], curwork)
        res_profit -= get_profit(curwork)
    return

do_work(1,0)
print(result)