# 백준 10989 => 수 정렬하기 3  (계수 정렬)
import sys
input = sys.stdin.readline

N = int(input())   # 정렬할 수 개수
count = [0] * 10001   # 카운팅 정렬 리스트

for i in range(N):   # 천만번
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)