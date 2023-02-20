# 백준 1253 좋은수 구하기  == 입력받은 수 중 서로다른 두수의 합으로 입력수가 나오면 좋은수
import sys
input = sys.stdin.readline

N = int(input())    # 입력 데이터 개수
count = 0
A = list(map(int, input().split()))   # 한줄에 입력을 다 받을때 사용
A.sort()   # 전체 정렬

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1  # i는 리스트 첫번째, j는 리스트 마지막번째 위치
    while i < j:   # 두 인덱스가 만나게되면 while문을 종료
        if A[i] + A[j] == find:
            if i != k and j != k:    # i와 j는 k와 같은위치가 되면 안됨
                count += 1
                break
            elif i == k:  i += 1
            elif j == k:  j -= 1
        elif A[i] + A[j] < find:   # i를 증가시켜야 합의수가 커짐
            i += 1
        elif A[i] + A[j] > find:
            j -= 1    # i값과 j값을 더한값이 find보다 크면 j의 값을 낮춰줘야함!

print(count)




