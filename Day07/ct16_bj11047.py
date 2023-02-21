# 백준 11047 동전 개수 최소값
N, K = map(int, input().split())   # N : 동전의 개수(10), K : 목표 금액(4750)
A = [0] * N  # 동전 데이터 리스트

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N -1 , -1, -1):  # 역순으로
    if A[i] <= K:   # 현재 동전 가치가 K보다 작거나 같으면
        count += K // A[i]
        K = K % A[i]  # 현재동전 나머지를 금액으로 업데이트

print(count)
