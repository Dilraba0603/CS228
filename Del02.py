import sys
sys.path.insert(0,'..')
import Leap
from pygameWindow import PYGAME_WINDOW
import random
from constants import pygameWindowWidth, pygameWindowDepth

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
    #global x,y,xMin,xMax,yMin,yMax
    #hand = frame.hands[0]
    fingers = hand.fingers
    
    for finger in fingers:
        
        Handle_Finger(finger)
        #for b in range(4):
            
            #Handle_Bone(bone)
            #bone = finger.bone(b)
            #print(bone)
            
    #indexFingerList = fingers.finger_type(0)
    #indexFinger = indexFingerList[0]
    #distalPhalanx = indexFinger.bone(0)
    #tip = distalPhalanx.next_joint
    #x=int(tip[0])
    #y=int(tip[1])
    #if (x<xMin):
     #   xMIn=x
    #if (x>xMax):
    #    xMax=x
    #if (y<yMin):
    #    yMIn=y
    #if (y>yMax):
    #    yMax=y    
    #return x,y

            
        
    pass
def Handle_Finger(finger):
    for b in range(4):
        
        Handle_Bone(b,finger)
        #bone = finger.bone(b)
        #print(bone)
    pass
        
def Handle_Bone(b,finger):
    bone = finger.bone(b)
    #Handle_Vector_From_Leap(v)
    base = bone.next_joint
    [base_x,base_y] = Handle_Vector_From_Leap(base)
    
    #Handle_Vector_From_Leap(v)
    tip = bone.prev_joint
    [tip_x,tip_y] = Handle_Vector_From_Leap(tip)
    pygameWindow.Draw_Black_Line(base_x,base_y,tip_x,tip_y)
    
    
    #print (bone)
    pass
def Handle_Vector_From_Leap(v):
        global x,y,xMin,xMax,yMin,yMax
        x = int(v[0])
        y = int(v[2])
        if(x < xMin):
                xMin = x
        if(x > xMax):
                xMax = x
        if(y<yMin):
                yMin = y
        if(y>yMax):
                yMax = y
        pygameX = int(scaleFunction(x,xMin,xMax,0,pygameWindowWidth))
        pygameY = int(scaleFunction(y,yMin,yMax,0,pygameWindowDepth))
        return pygameX,pygameY
def scaleFunction(a,b,c,d,e):
        test = c-b
        if(test==0):
                a = d
        else:
                a =((a-b)/float((c-b)))*(e-d)+d
        return a
    
controller = Leap.Controller()
while True:
    pygameWindow.Prepare()
    frame = controller.frame()
       
    if (frame>0):
        handlist = frame.hands
        for hand in handlist:
            Handle_Frame(frame)
            
            pygameX=int(scaleFunction(x,xMin,xMax,pygameWindowWidth,pygameWindowDepth))
            pygameY=int(scaleFunction(y,yMin,yMax,pygameWindowWidth,pygameWindowDepth))
                        
       
        
        
        
    
    #Perturb_Circle_Position()
    #pygameWindow.Draw_Black_Circle(pygameWindow,(0,0,0),(pygameX,pygameY),20)
    pygameWindow.Reveal()
print(pygameWindow)
