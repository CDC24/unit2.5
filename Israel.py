#Caleb Callaway
#3/7/18
#Israel.py - uses ggame to display Israeli flag


from ggame import *

black = Color(0X00000000,1)
white = Color(0XFFFFFF,1)

blackline = LineStyle(1,black)
whiteline = LineStyle(1,white)

backRectangle = RectangleAsset(1100,1000, blackline, black)
whiteRectangle = RectangleAsset(500,300, whiteline, white)

Sprite (backRectangle)
Sprite (whiteRectangle)



App().run()