# 백준 1929 => 소수 구하기
import math
M , N = map(int, input().split())   # M은 시작수, N은 종료수
A = [0] * (N + 1)  # 초기화

for i in range(2, N +1):   
    A[i] = i   # 인덱스 채워넣기

for i in range(2, int(math.sqrt(N)) + 1):   # N의 제곱근까지만 수행 (루트)
    if A[i] == 0:
        continue    
    for j in range(i + i, N + 1, i):   # 배수로 값을 지우기
        A[j] = 0   # 소수가 아닌 것은 지운다

for i in range(M, N+1):
    if A[i] != 0:
        print(A[i])

