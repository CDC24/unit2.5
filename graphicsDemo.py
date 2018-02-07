#Caleb Callaway
#2/7/18
#graphicsDemo.py - intro to ggame: Mr.Dennison's graphics package

from ggame import *
#the asterisk imports the whole thing


red = Color(0xFF0000,1) # (RGB code, opacity)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0X00000000,1)

blackOutline = LineStyle(1,black)
redRectangle = RectangleAsset(100,300, blackOutline, red) #(width,height,outline,fill)
blueCircle = CircleAsset(100,blackOutline, blue) #(radius,outline,fill)


Sprite(redRectangle)
Sprite(blueCircle)

App().run()
