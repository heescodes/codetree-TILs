# 변수 선언 및 입력

n, m = tuple(map(int, input().split()))
combination = []


# 방문한 원소들을 출력해줍니다.
def print_combination():
    for elem in combination:
        print(elem, end = " ")
    
    print()


def find_combination(curr_num, cnt):
    # n개의 숫자를 모두 탐색했으면 더 이상 탐색하지 않습니다.
    if curr_num == n + 1:
        # 탐색하는 과정에서 m개의 숫자를 뽑은 경우 답을 출력해줍니다.
        if cnt == m:
            print_combination()
        return

    # curr_num에 해당하는 숫자를 사용했을 때의 경우를 탐색합니다.
    combination.append(curr_num)
    find_combination(curr_num + 1, cnt + 1)
    combination.pop()

    # curr_num에 해당하는 숫자를 사용하지 않았을 때의 경우를 탐색합니다.
    find_combination(curr_num + 1, cnt)


find_combination(1, 0)