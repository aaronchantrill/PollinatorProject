#!/usr/bin/env python3

import cv2
import numpy as np

# The filename should be passed as a parameter,
# but I was too lazy to write that so I just
# kept editing the following line every time
# I switched files.
videofile = '2019-10-15_10.00.02_68.mp4'
cap = cv2.VideoCapture(videofile)

if( cap.isOpened() == False ):
    print("Error opening video file")
else:
    count = 0
    frame_no = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame_no += 1
            cv2.rectangle(
                frame,
                (5,350),    # Upper left corner
                (335,450),  # Lower right corner
                (255,0,0),  # Blue (BGR)
                3           # border width
            )
            cv2.imshow(videofile,frame)
            key=cv2.waitKey(0) & 0xFF
            if key == ord('q'):
                break
            if key == 82:  # up arrow (count 1 hit)
                count += 1
                print(count)
            if key == 81:  # left arrow (rewind 1 frame)
                frame_no-=2
                if(frame_no < 0):
                    frame_no = 0
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            if key == ord('p'):  # take a screen capture
                cv2.imwrite("{}_{}.jpg".format(videofile,frame_no), frame)
        else:
            break
cap.release()
cv2.destroyAllWindows()
