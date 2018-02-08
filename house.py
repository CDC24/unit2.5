#Caleb Callaway
#2/8/18
#house.py - displays a house using ggame



from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0X00000000,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(1,black)
redRectangle = RectangleAsset(200,150, blackOutline, red) #(width,height,outline,fill)
blackTriangle = PolygonAsset([(150,0),(0,150),(300,150)],blackOutline,black)#([relative vertex coordintates],etc)
yellowRectangle = RectangleAsset(40,50, blackOutline, yellow)

Sprite(redRectangle,(150,350))
Sprite(blackTriangle,(100,200))
Sprite(yellowRectangle,(170,400))

App().run()
