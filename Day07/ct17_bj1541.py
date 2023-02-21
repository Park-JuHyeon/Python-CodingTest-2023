# 백준 1541번 => 잃어버린 괄호

answer = 0
A = list(map(str, input().split('-')))   # - 를 기준으로 잘라서 문자열로 리스트

def mySum(i):   # -로 나눈 각 수식 문자열 합구하기 함수
    result = 0
    temp = str(i).split('+')   # +기준으로 수식을 자른다
    for k in temp:
        result += int(k)   # 그냥 k는 '78' 문자열 이므로 int로 형변환 해줘야함

    return result 

for s in range(len(A)):
    temp = mySum(A[s])
    if s == 0 :
        answer += temp
    else:
        answer -= temp

print(answer)






