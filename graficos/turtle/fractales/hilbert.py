from turtle import * 
  
def hilbert(level, angle, step):
    if level == 0:
        return
  
    right(angle)
    hilbert(level-1, -angle, step)
  
    forward(step)
    left(angle)
    hilbert(level-1, angle, step)
  
    forward(step)
    hilbert(level-1, angle, step)
  
    left(angle)
    forward(step)
    hilbert(level-1, -angle, step)
    right(angle)


tracer(0,0)
level = 4
size = 200

def init():
    global size
    penup()
    goto(-size / 2.0, size / 2.0)
    pendown()

def nivelmas():
    global level
    clear()
    init()
    level += 1
    hilbert(level, 90, size/(2**level-1))
    update()
    
def nivelmenos():
    global level
    clear()
    init()
    level -= 1
    hilbert(level, 90, size/(2**level-1))
    update()

onkey(nivelmas, 'a')
onkey(nivelmenos, 'd')
listen()


 

hilbert(level, 90, size/(2**level-1))


