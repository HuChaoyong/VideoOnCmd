#! encoding: UTF-8
import cv2
video_path = "./video/badapple.mp4"
cap = cv2.VideoCapture(video_path)
success = True
while(success):
    success, frame = cap.read()
    if  success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        s = ''
        for r in range(0, gray.shape[0], 6):
            for c in range(0, gray.shape[1], 3):
                if gray[r, c] > 200:
                    s += ' '
                else:
                    s += '0'
            s += '\n'
        print(s)
cap.release()
