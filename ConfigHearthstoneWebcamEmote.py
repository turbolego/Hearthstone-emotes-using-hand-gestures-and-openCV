#!/usr/bin/python
import sys
import os
from Tkinter import *
import tkMessageBox
root = Tk()
root.wm_title("Config for Hearthstone WebCam Emote")
Label(text= "Click on your screen resolution, then click the Start button:").grid(row=0, columnspan=6)
# frame = Frame(root)
# frame.pack()

# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )

def start():
    os.system('python HearthstoneWebcamEmote.py')

def config_1024x768():
    f = open('screensize.py','w')
    f.write('xsize = 512' + '\n' + 'ysize = 580')
    f.close()
def config_1360x768():
    f = open('screensize.py','w')
    f.write('xsize = 1360' + '\n' + 'ysize = 768')
    f.close()
def config_1366x768():
    f = open('screensize.py','w')
    f.write('xsize = 1366' + '\n' + 'ysize = 768')
    f.close()
def config_1280x800():
    f = open('screensize.py','w')
    f.write('xsize = 1280' + '\n' + 'ysize = 800')
    f.close()
def config_1152x864():
    f = open('screensize.py','w')
    f.write('xsize = 1152' + '\n' + 'ysize = 864')
    f.close()
def config_1440x900():
    f = open('screensize.py','w')
    f.write('xsize = 1440' + '\n' + 'ysize = 900')
    f.close()
def config_1280x960():
    f = open('screensize.py','w')
    f.write('xsize = 1280' + '\n' + 'ysize = 960')
    f.close()
def config_1600x900():
    f = open('screensize.py','w')
    f.write('xsize = 1600' + '\n' + 'ysize = 900')
    f.close()
def config_1400x1050():
    f = open('screensize.py','w')
    f.write('xsize = 1400' + '\n' + 'ysize = 1050')
    f.close()
def config_1680x1050():
    f = open('screensize.py','w')
    f.write('right_x = 840' + '\n' + 'right_y = 800' + '\n' + 'left_x = 650' + '\n' + 'left_y = 840')
    f.close()
def config_1920x1080():
    f = open('screensize.py','w')
    f.write('right_x = 960' + '\n' + 'right_y = 825' + '\n' + 'left_x = 760' + '\n' + 'left_y = 860')
    f.close()

Button(text="Start",command= start).grid(row=0,column=6)
# Start.pack(side = TOP)
	
Button(text="1024x768", command= config_1024x768).grid(row=1,column=0)
# Res1.pack(side = LEFT)

Button(text="1360x768",command= config_1360x768).grid(row=1,column=1)
# Res2.pack(side = LEFT)

Button(text="1366x768",command= config_1366x768).grid(row=1,column=2)
# Res3.pack(side = LEFT)

Button(text="1280x800",command= config_1280x800).grid(row=1,column=3)
# Res4.pack(side = LEFT)

Button(text="1152x864",command= config_1152x864).grid(row=1,column=4)
# Res5.pack(side = LEFT)

Button(text="1440x900",command= config_1440x900).grid(row=1,column=5)
# Res6.pack(side = LEFT)

Button(text="1280x960",command= config_1280x960).grid(row=2,column=0)
# Res7.pack(side = LEFT)

Button(text="1600x900",command= config_1600x900).grid(row=2,column=1)
# Res8.pack(side = LEFT)

Button(text="1400x1050",command= config_1400x1050).grid(row=2,column=2)
# Res9.pack(side = LEFT)

Button(text="1680x1050",command= config_1680x1050).grid(row=2,column=3)
# Res10.pack(side = LEFT)

Button(text="1920x1080",command= config_1920x1080).grid(row=2,column=4)
# Res11.pack(side = LEFT)

root.mainloop()