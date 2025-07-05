from turtle import*

speed(1000)
bgcolor("black")
pensize(2)
pencolor("#306998")

def curve1():
    for i in range(90):
        left(1)
        forward(1)

def curve2():
    for i in range(90):
        right(1)
        forward(1)  

def curve3():
    curve1()
    forward(80)
    curve1()

def curve4():
    curve1()
    forward(90)
    curve1()

def half():
    forward(50)
    curve1() 
    forward(90)
    curve3() 
    forward(40)
    left(90)
    forward(80)
    right(90)
    forward(10)
    right(90)
    forward(120)
    curve4()
    forward(30)
    left(90)
    forward(50)
    curve2()
    forward(40)
    end_fill()

def get_pos():
    penup()
    forward(20)
    right(90)
    forward(10)
    right(90)
    pendown()

def eye():
    penup()
    right(90)
    forward(160)
    left(90)
    forward(70)
    pencolor("black")
    dot(35)

def sec_dot():
    left(90)
    penup()
    forward(310)
    left(90)
    forward(120)
    pendown()

    dot(35)

fillcolor("#306998")
begin_fill()

half()
end_fill()
get_pos()
pencolor("#FFD43B")
fillcolor("#FFD43B")
begin_fill()
half()
end_fill()

eye()
sec_dot()

mainloop()