#!/usr/bin/env python3

import cv2
import numpy as np

video = '2019-10-20_16.00.03_68.0.mp4'
cap = cv2.VideoCapture(video)

if( cap.isOpened() == False ):
    print("Error opening video file")
else:
    count=0;
    frame_no=0;
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame_no+=1
            cv2.rectangle(
                frame,
                (5,350),
                (335,450),
                (255,0,0),
                3
            )
            cv2.imshow("{}".format(video),frame)
            key = cv2.waitKey(25) & 0xFF
            # print("Key: {}".format(key))
            if key == ord('q'):
                break
            if key == 82:
                count+=1
                print(count)
            if key == 81:
                # rewind 100 frames
                frame_no-=100
                if frame_no < 0:
                    frame_no=0
                cap.set(cv2.CAP_PROP_POS_FRAMES,frame_no)
        else:
            break
cap.release()
cv2.destroyAllWindows()

