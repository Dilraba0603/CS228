import numpy
import pickle
import os
from pygameWindow_sample import PYGAME_WINDOW
from constants import *
import time
#from Deliverable_sample import DELIVERABLE
class READER:

    def __init__(self):
        self.numGestures = 0
        self.Get_Num_Gestures()
        self.pygameWindow = PYGAME_WINDOW()
        #self.deliverable = DELIVERABLE()
        self.RMAX=100
        self.RMIN=200

    # scale leap coords to pygame coords
    def Scale(self, val, tMin, tMax):
        if (self.RMAX == self.RMIN):
            return 0
        return (int)(tMax - tMin) * (val - self.RMIN) / (self.RMAX - self.RMIN) + tMin

    def Get_Num_Gestures(self):
        path, dirs, files = next(os.walk("userData"))
        self.numGestures = len(files)

    def Print_Gestures(self):
        for i in range(self.numGestures):
            pickle_in = open("userData/gesture" + str(i) + ".p", "rb")
            gestureData = pickle.load(pickle_in)
            pickle_in.close()
            print(gestureData)

    def Draw_Gesture(self, currGesture):
        self.pygameWindow.Prepare()
        print(currGesture)
        pickle_in = open("userData/gesture" + str(currGesture) + ".p", "rb")
        gestureData = pickle.load(pickle_in)
        pickle_in.close()
        r = 0
        g = 255
        b = 0
        #if(self.deliverable.currNumberOfHands == 2):
            #r = 255
            #g = 0
            #b = 0
        for i in range(5):
            for j in range(4):
                currentBone = gestureData[i,j,:]
                xBaseNotYetScaled = currentBone[0]
                yBaseNotYetScaled = currentBone[2]
                xTipNotYetScaled = currentBone[3]
                yTipNotYetScaled = currentBone[5]
                xBase = self.Scale(xBaseNotYetScaled, 0, pygameWindowWidth)
                yBase = self.Scale(yBaseNotYetScaled, 0, pygameWindowDepth)
                xTip = self.Scale(xTipNotYetScaled, 0, pygameWindowWidth)
                yTip = self.Scale(yTipNotYetScaled, 0, pygameWindowDepth)
                
                self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, 2,r,g,b)
                #pygame.draw.line(self.screen, (r,g,b), (baseX, baseY), (tipX, tipY), width)
                #Draw_Line(self, baseX, baseY, tipX, tipY, width, r, g, b):

        self.pygameWindow.Reveal()
        time.sleep(0.2)

    def Draw_Each_Gesture_Once(self):
        for i in range(self.numGestures):
            self.Draw_Gesture(i)

    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()
