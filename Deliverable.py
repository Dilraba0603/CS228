import sys
sys.path.insert(0,'..')
import Leap
import numpy as np

from pygameWindow_Del03 import PYGAME_WINDOW 
from constants import pygameWindowWidth, pygameWindowDepth
class DELIVERABLE:
    def __init__ (self):
        self.xMin=500
        self.xMax=-500
        self.yMin=500
        self.yMax=-500
        self.x=250
        self.y=250
        self.controller= Leap.Controller()
        self.pygameWindow=PYGAME_WINDOW()
        self.previousNumberOfHands=0
        self.currentNumberOfHands=0
        self.gestureData = np.zeros((5,4,6),dtype='f')
        self.fileIndex = 0
        self.Recreate_userData_Directory()
    def Recording_Is_Ending(self):
        if self.currentNumberOfHands==1:
            return True
        elif self.currentNumberOfHands==1:
            return False
    def Handle_Frame(self,frame):
        
        self.currentNumberOfHands =len(frame.hands)
        
        hand = frame.hands[0]
        
        fingers = hand.fingers
    
        for finger in fingers:
        
             self.Handle_Finger(finger)
        
        if self.Recording_Is_Ending():
             #print('recording is ending.')
             #print(self.gestureData[0,:,:])
            print(self.gestureData[0,3,3:6])
        
    
    def Handle_Finger(self,finger):
        for b in range(4):
        
            self.Handle_Bone(b,finger)
        
    
        
    def Handle_Bone(self,b,finger):
        bone = finger.bone(b)
    
        base = bone.prev_joint
        tip = bone.next_joint
        if self.Recording_Is_Ending():           
            self.gestureData[i,j,0] = base[0]
            self.gestureData[i,j,1] = base[1]
            self.gestureData[i,j,2] = base[2]
            
            self.gestureData[i,j,3] = tip[0]
            self.gestureData[i,j,4] = tip[1]
            self.gestureData[i,j,5] = tip[2]
        [base_x,base_y] = self.Handle_Vector_From_Leap(base)
    
    
        
        [tip_x,tip_y] = self.Handle_Vector_From_Leap(tip)
        r=0
        g=0
        b=0
        if(self.currNumberOfHands == 2):
            r = 255
            g = 0
            b = 0
        self.pygameWindow.Draw_Line(color,base_x,base_y,tip_x,tip_y,r,g,b)
        
    
    
    
    
    def Handle_Vector_From_Leap(self,v):
        
        
        self.x = int(v[0])
        self.y = int(v[2])
        if(self.x < self.xMin):
                self.xMin = self.x
        if(self.x > self.xMax):
                self.xMax = self.x
        if(self.y<self.yMin):
                self.yMin = self.y
        if(self.y>self.yMax):
                self.yMax = self.y
        pygameX = int(self.scaleFunction(self.x,self.xMin,self.xMax,0,pygameWindowWidth))
        pygameY = int(self.scaleFunction(self.y,self.yMin,self.yMax,0,pygameWindowDepth))
        return pygameX,pygameY
    def scaleFunction(self,a,b,c,d,e):
        test = c-b
        if(test==0):
                a = d
        else:
                a =((a-b)/float((c-b)))*(e-d)+d
        return a
        
    def Run_Forever(self):
        
        while True:
            self.Run_Once()
    def Run_Once(self):
        self.pygameWindow.Prepare()
            
        frame = self.controller.frame()
        handlist = frame.hands
        if not handlist:
            print("no hand")
        else:
            num = 0
        for hand in handlist:
            num+=1
            if(num>0):
                self.Handle_Frame(frame)
        self.pygameWindow.Reveal()
            
