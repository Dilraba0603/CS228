import sys
sys.path.insert(0,'..')
import Leap
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowWidth, pygameWindowDepth
import random

xMin=500.0
xMax=-500.0
yMin=500.0
yMax=-500.0

pygameWindow=PYGAME_WINDOW()
global pygameX,pygameY
pygameX=250
pygameY=250
x=250
y=250
#def Perturb_Circle_Position():
    #global x,y
    #fourSidedDieRol=random.randint(1,4)
    #if fourSidedDieRol==1:
        #x-=1
    #elif fourSidedDieRol==2:
        #x+=1
    #elif fourSidedDieRol==3:
        #y-=1
    #else:
        #y+=1
    #return x,y
def Handle_Frame(frame):
    global x,y,xMin,xMax,yMin,yMax
    hand = frame.hands[0]
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(0)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(0)
    tip = distalPhalanx.next_joint
    x=int(tip[0])
    y=int(tip[1])
    if (x<xMin):
        xMIn=x
    if (x>xMax):
        xMax=x
    if (y<yMin):
        yMIn=y
    if (y>yMax):
        yMax=y

    
    return x,y 

def scaleFunction(x, xMin, xMax, a, b):
    
    result = (b - a) * ((x - xMin) / (xMax - xMin)) + a
    return result
    
controller = Leap.Controller()
while True:
    
    frame = controller.frame()
       
    if (frame>0):
        handlist = frame.hands
        for hand in handlist:
            Handle_Frame(frame)
            
            pygameX=int(scaleFunction(x,xMin,xMax,-200,300))
            pygameY=int(scaleFunction(y,yMin,yMax,-200,300))
                       
       
        
        
        
    pygameWindow.Prepare()
    #Perturb_Circle_Position()
    pygameWindow.Draw_Black_Circle(pygameWindow,(0,0,0),(pygameX,pygameY),20)
    pygameWindow.Reveal()
print(pygameWindow)

