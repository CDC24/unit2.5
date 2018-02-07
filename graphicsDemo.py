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
greenEllipse = EllipseAsset(150,50,blackOutline, green) #(width,height,outline,fill)
blackLine = LineAsset(300,400,blackOutline) #(x endpoint,y endpoint,>>starting from top left!!<< line style)


Sprite(redRectangle)
Sprite(blueCircle,(200,100))#(blue is new coordinates, 200 TO THE RIGHT, 100 DOWN)
Sprite(greenEllipse,(50,300))
Sprite(blackLine)

App().run()
