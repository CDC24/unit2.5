#Caleb Callaway
#3/7/18
#name.py - uses ggame to display name and backround RGB color



from ggame import *

RGB = input("Enter a 6-digit RGB color code.")

Color = Color(0x(RGB),1)

colorRectangle = RectangleAsset(900,900, Color)

Sprite (colorRectangle)


App().run()
