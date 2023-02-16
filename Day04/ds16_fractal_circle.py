# 프랙탈 원 그리기
import tkinter
import turtle   # 그림그려주는 거북이

turtle.setup(width=600, height= 600)
t = turtle.Turtle()   # 거북이만들기
t.shape('turtle')

c = t.clone()    # 거북이 복제
c.color('blue')
c.circle(30)

for i in range(4,10):
    c.circle(i * 10)

turtle.mainloop()
