import sys
sys.path.insert(0,'..')
import Leap
controller = Leap.Controller()
from pygameWindow import PYGAME_WINDOW
import random
from constants import pygameWindowWidth, pygameWindowDepth 
pygameWindow = PYGAME_WINDOW()
#print(pygameWindow)
#x,y coordinate
x = 450
y = 450
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0
def Handle_Frame(frame):
        global x,y,xMin,xMax,yMin,yMax
        hand = frame.hands[0]
        fingers = hand.fingers
        for finger in fingers:
                Handle_Finger(finger)
def ScaleFiveArgu(a,b,c,d,e):
        test = c-b
        if(test==0):
                a = d
        else:
                a =((a-b)/float((c-b)))*(e-d)+d
        return a
def ScaleForZ(a,b,c,d,e):
        test = c-b
        if(test==0):
                a = d
        else:
                a = ((1-1.75*(a/ float(c - b))) * (e-d))
        return a
def Handle_Finger(finger):
        for b in range(0,4):
                Handle_Bone(b,finger)
def Handle_Bone(b,finger):
        global x,y,xMin,xMax,yMin,yMax
        bone = finger.bone(b)
        base = bone.prev_joint
        tip = bone.next_joint
        [base_x,base_y] = Handle_Vector_From_Leap(base)
        [tip_x,tip_y] = Handle_Vector_From_Leap(tip)
        pygameWindow.Draw_Black_Line(base_x,base_y,tip_x,tip_y)
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
        windowX = int(ScaleFiveArgu(x,xMin,xMax,0,pygameWindowWidth))
        windowY = int(ScaleFiveArgu(y,yMin,yMax,0,pygameWindowDepth))
        return windowX,windowY
while True:
        pygameWindow.Prepare()
        controller = Leap.Controller()
        frame = controller.frame()
        handlist = frame.hands
        if not handlist:
                print("no hand")
        else:
                num = 0
        for hand in handlist:
                num+=1
                if(num>0):
                        Handle_Frame(frame)
        pygameWindow.Reveal()
