#Caleb Callaway
#2/7/18
#graphicsDemo.py - intro to ggame: Mr.Dennison's graphics package

from ggame import *
#the asterisk imports the whole thing


red = Color(0xFF0000,1)
black = Color(0X00000000,1)

blackOutline = LineStyle(1,black)
redRectangle = RectangleAsset(200,300, blackOutline, red) #(width,height,outline,fill)


App().run()
