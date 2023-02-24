def solution2(n, lost, reserve):
    n_lost = set(lost) - set(reserve)   # 중복값 제거
    n_reserve = set(reserve) - set(lost)
    
    for i in n_lost:
        if i + 1 in n_reserve:
            n_reserve.remove(i + 1)
        elif i - 1 in n_reserve:
            n_reserve.remove(i - 1)
        else:
            n -= 1

    return n

n = 5
lost = [2, 4]
reserve = [3, 1, 5]

print(solution2(n, lost, reserve)) # return 5


n = 5
lost = [2, 4]
reserve = [3]

print(solution2(n, lost, reserve)) # return 4


n = 3
lost = [3]
reserve = [1]

print(solution2(n, lost, reserve)) # return 2