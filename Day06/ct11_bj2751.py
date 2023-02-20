# 백준 2751 => 수 정렬하기 2 (병합정렬)
# 1000000000000 1조개의 처리 시간복잡도가 O(n^2)은 불가
import sys
input = sys.stdin.readline
print = sys.stdout.write

A = []
tmp = []

def merge_sort(s, e):   # 합병정렬 소스 스타트  s = 시작점  e = 종료점
    if e - s < 1 : return
    m = int(s + (e - s)/ 2)    # m = 중간점
    merge_sort(s, m)  
    merge_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    index1 = s    # index1이 앞그룹 시작점에서 중간점 까지
    index2 = m + 1   # 중간값 이후 뒤쪽그룹
    while index1 <= m and index2 <= e:   # 두그룹을 병합
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:    # 한쪽그룹 모두 선택된 후 남아있는 값 정리.
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')







