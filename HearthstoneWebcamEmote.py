#!/usr/bin/env python2
"""
This is me messing around with OpenCV.
Hand gestures --> WebCam --> Emotes in Hearthstone! :D
"""

import cv2
from pymouse import PyMouse
from screensize import *

# PyMouse for moving the mouse and clicking mousebuttons. 
m = PyMouse()

# Haar cascade classifier XML-file for "Greetings" Emote, which i have trained to be a open hand.
GREETINGS_XML = "myfacedetector.xml"
#GREETINGS_XML = "hearthstone.xml"


classifier_greetings = cv2.CascadeClassifier(GREETINGS_XML)
Scale = 4

# Opening the webcam and running a while loop as long as the webcam is active.
video = cv2.VideoCapture(0)
if video.isOpened():
    active, frame = video.read()
else:
    active = False
while active:

# Downscaling and resizing fetched frames.

    Set_Scale = (frame.shape[1]/Scale,frame.shape[0]/Scale)
    Set_Size = cv2.resize(frame, Set_Scale)	
    greetings = classifier_greetings.detectMultiScale(Set_Size)

# For loop that activates mouse-movements and mouse-clicks which activates Emotes in Hearthstone.
# The for loop checks for the "Greetings" haarcascade classifier and compares it with fetched frames.
	
    for f in greetings:
        x, y, w, h = [ v*Scale for v in f ]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255))
        print "Greetings"
        m.move(right_x,right_y)
        cv2.waitKey(30)
        m.click(right_x,right_y,2)
        cv2.waitKey(30)
        m.move(left_x,left_y)
        cv2.waitKey(30)
        m.click(left_x,left_y,1)

# Adding a text overlay to the webcam preview window
    cv2.putText(frame, "Hit the ESC key to quit.", (10, 30),
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255,255,255))

# Webcam preview window label
    cv2.imshow("I see you", frame)

# Fetching the next frame.
    active, frame = video.read()


# If the user hits the ESc key, the program quits.
    key = cv2.waitKey(20)
    if key in [27, ord('Q'), ord('q')]:
        break