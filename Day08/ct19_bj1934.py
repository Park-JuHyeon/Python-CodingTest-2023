# 백준 1934 최소공배수 구하기 , 최대공약수 활용!

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b)
    print(int(result))