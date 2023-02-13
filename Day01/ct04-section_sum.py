# 입력속도 개선! , 단 주피터에서는 실행불가
import sys
input = sys.stdin.readline  # 이부분없으면 백준 통과불가!

N, M = tuple(map(int, input().split()))   # N = 데이터의 개수 , M = 계산할 개수
numbers = list(map(int, input().split()))  # 숫자 리스트 [1 2 3 4 5] 같은
sums = [0]   # 배열 0번째 인덱스 값 핵심!!
temp = 0

for i in numbers:
    temp = temp + i  # temp 5 9 12 14 15 순서로
    sums.append(temp)
    # [0, 5, 9, 12, 14, 15]

for i in range(M):
    x, y = tuple(map(int, input().split()))
    print(sums[y] - sums[x - 1])
    
