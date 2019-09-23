from pygameWindow import PYGAME_WINDOW
import random
pygameWindow=PYGAME_WINDOW()

x=250
y=250
def Perturb_Circle_Position():
    global x,y
    fourSidedDieRol=random.randint(1,4)
    if fourSidedDieRol==1:
        x-=1
    elif fourSidedDieRol==2:
        x+=1
    elif fourSidedDieRol==3:
        y-=1
    else:
        y+=1
    return x,y

while True:
    
    pygameWindow.Prepare()
    Perturb_Circle_Position()
    pygameWindow.Draw_Black_Circle(pygameWindow,(0,0,0),(x,y),20)
    pygameWindow.Reveal()
print(pygameWindow)


    
