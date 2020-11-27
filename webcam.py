import cv2
from collections import deque
import numpy as np
import time
import os

class Webcam:

    def __init__(self):
        self.video_filename = 'video.avi'
        self.video_counter = 0
        self.video_capture_duration = 10
        self.frames = deque(maxlen=2)
        self.maxError = 2000     # the max difference between 2 frames 
        self.movement_detected = False 
        self.frames_per_second = 24.0
        self.res = '720p'
        self.VIDEO_TYPE = {
                'avi': cv2.VideoWriter_fourcc(*'XVID'),
                #'mp4': cv2.VideoWriter_fourcc(*'H264'),
                'mp4': cv2.VideoWriter_fourcc(*'XVID'),
        }
        self.STD_DIMENSIONS =  {
                "480p": (640, 480),
                "720p": (1280, 720),
                "1080p": (1920, 1080),
                "4k": (3840, 2160),
        }

    def compare_frames(self):
        # estiamtes the difference between two images using "mean square error"
        frame1 = np.asarray(self.frames[0])
        frame2 = np.asarray(self.frames[1])
        error = np.sum((frame1.astype("float") - frame2.astype("float")) ** 2)
        error /= float(frame1.shape[0] * frame1.shape[1])
        print ("Difference between last 2 frames: " + str(error))
        if error > self.maxError:
	    self.movement_detected = True
    
    def capture_frame(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        self.frames.append(frame)
        cap.release()
    
    def change_res(self, cap, width, height):
        cap.set(3, width)
        cap.set(4, height)

    def get_dims(self, cap, res='1080p'):
        width, height = self.STD_DIMENSIONS["480p"]
        if res in self.STD_DIMENSIONS:
	    width,height = self.STD_DIMENSIONS[res]
        self.change_res(cap, width, height)
        return width, height

    def get_video_type(self, video_filename):
        filename, ext = os.path.splitext(video_filename)
        if ext in self.VIDEO_TYPE:
            return  self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']
            
    def record_video(self):     
        cap = cv2.VideoCapture(0)
        out = cv2.VideoWriter("(" + str(self.video_counter) + ")" + self.video_filename, self.get_video_type(self.video_filename), 25, self.get_dims(cap, self.res))
        start_time = time.time()
        while(int(time.time() - start_time) < self.video_capture_duration):
            ret, frame = cap.read()
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
		break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        cv2.waitKey(10000)
        self.video_counter += 1

if __name__ == "__main__":
    webcam = Webcam()
    while (True):
        if input("Are you ready to start the script? [y/n]: ").lower() == "y":
            print("Script will start in 10 seconds...")
            time.sleep(10)
            break
    while (True):
        webcam.capture_frame()
        webcam.capture_frame()
        webcam.compare_frames()
        if webcam.movement_detected == True:
            webcam.record_video()
            webcam.movement_detected = False
