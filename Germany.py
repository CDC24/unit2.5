#Caleb Callaway
#2/9/18
#germany.py - uses ggame to display a german flag


from ggame import *


black = Color(0x000000,1)
red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(0,black)
blackRectangle = RectangleAsset(500,100, blackOutline, black)
redRectangle = RectangleAsset(500,100, blackOutline, red)
yellowRectangle = RectangleAsset(500,100, blackOutline, yellow)

text = textAsset ("DEUTSCHLAAAAAAAAAAAAAAAAAAAAAAND!!!", fill=black, style="bold 800 pt Times")

Sprite (blackRectangle,(100,100))
Sprite (redRectangle,(100,200))
Sprite (yellowRectangle,(100,300))
sprite (text, (100, 500)

App().run()