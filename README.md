# Hearthstone-emotes-using-hand-gestures-and-openCV
This is a short test for hearthstone emotes using hand gestures and openCV.
Coded by Tobias Andersen and designed by Sindre Säfvenbom.

# Requisites:

1. [OpenCV 2.2](http://opencv.org/downloads.html)
2. [Python 2.7](https://www.python.org/)
3. [Hearthstone](http://us.battle.net/hearthstone/en/)
4. Webcam

# First time use:

1. Run "ConfigHearthstoneWebcamEmote.py" and select the screen resolution you have when playing hearthstone.
2. Click "Start"
3. Play Hearthstone and show your hand to activate the emote for "Greetings"

# Use with the same configuration:

1. Run "HearthstoneWebcamEmote.py"
2. Play Hearthstone and show your hand to activate the emote for "Greetings"

# Demo:

[Youtube - OpenCV test #1: Hearthstone Emotes using Webcam!](https://www.youtube.com/watch?v=DuG9nvdnLBI)

# Notes:
The included classifiers (hearthstone.xml and myfacedetector.xml) were made under light and hue conditions that may be different from yours. This may affect the precision.
Both classifiers were made from scratch by using the guide written by Mahdi Rezaei from The Department of Computer Science, the University of Auckland.

Link to said guide: [Creating a Cascade of Haar-Like Classifiers: Step by Step](https://www.researchgate.net/publication/259584296_Tutorial-_Creating_a_Cascade_of_Haar-like_Classifiers_Step_by_Step)

You can change the classifier by editing line 15 in "HearthstoneWebcamEmote.py"
