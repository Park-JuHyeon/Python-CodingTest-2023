# 백준 1920 => 원하는 정수 찾기
N = int(input())  # 5
A = list(map(int,input().split()))   # 4 1 5 2 3
A.sort()   # 파이썬 리스트에서 제공하는 기본 정렬

M = int(input())  # 4
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    # 이진 탐색
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2   # 중앙 인덱스
        midVal = A[middle]   # 중앙에 있는 값
        if midVal > target:   # 오른쪽 날림
            end = middle - 1
        elif midVal < target:   # 왼쪽 날림
            start = middle + 1
        else:   # 값 찾음
            find = True
            break
    
    if find:
        print(1)
    else:
        print(0)



