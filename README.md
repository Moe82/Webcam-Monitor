***Code is currently very buggy and not ready to be used. Will update README.md after I fix the issues and implement all of the features.***
# Webcam-Monitor

A Python script that turns your webcam into a surveillance camera.  

## Requirements 
- Python 3
- [OpenCV](https://pypi.org/project/opencv-python/) library
- [Numpy](https://pypi.org/project/numpy/) library

## Installation 
Clone this repository and install the required packages:
```bash
git clone https://github.com/Moe82/Webcam-Monitor.git
pip install numpy
pip install opencv-python
``` 
Allow camera access for terminal (or whichever application you use to run the script).
 - instructions for [MacOS](https://apple.stackexchange.com/questions/360851/add-access-to-the-macbook-camera-for-the-terminal-application)

## Inspiration
Given how expensive security cameras can be, I wanted to see if I can leverage the functionality of a webcam (which I think most people have access to) in order to create a free security system that anyone can use.

## Features to be included
- Automatically uploads recorded footage to the cloud in case the machine gets stolen.
- Only records footage when a certain threshold is detected to minimize disk space used.
- Option to play an alarm when movement is detected. 
