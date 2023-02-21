# 프로그래머스 0단계 : 다음에 올 숫자 (등비, 등차)

def solution(common):
    answer = 0
    if common[2] - common[1] == common[1] - common[0]:
        answer = common[len(common) - 1] + common[1] - common[0]
    else:
        answer = common[len(common) - 1] * common[1] // common[0]
        
    return answer






    


    
   
