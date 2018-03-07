#Caleb Callaway
#3/7/18
#name.py - uses ggame to display name and backround RGB color



from ggame import *

RGB = input("Enter a 6-digit RGB color code.")

theColor = Color((RGB),1)
line = LineStyle(1,theColor)

colorRectangle = RectangleAsset(900,900, line, theColor)

Sprite (colorRectangle)


App().run()
