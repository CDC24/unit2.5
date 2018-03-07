#Caleb Callaway
#3/7/18
#name.py - uses ggame to display name and backround RGB color



from ggame import *

name= input ("What's yer name? ")

RGB = input("Enter a 6-digit RGB color code starting with 0x (ex. 0xFF0000) ")
black = Color(0X00000000,1)

theColor = Color((RGB),1)
line = LineStyle(1,theColor)

colorRectangle = RectangleAsset(1100,1000, line, theColor)
namewrite = TextAsset((name), fill=black, style="bold 400 pt Times")

Sprite (colorRectangle)


App().run()
