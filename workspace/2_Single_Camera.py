import numpy as np
import cv2


cap = cv2.VideoCapture(2)
# outcrop = cv2.VideoWriter('outcrop.mov', -1, 20.0, (640,480))

X = 1

def rescale_frame(frame, percent=100):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while True:
    ret, raw_frame = cap.read()
    # frame = raw_frame[100:200, 100:200]
    frame = raw_frame[:, :]
    # sky = cv2.resize(sky, (640, 480))


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    elif k == ord('1'): # wait for '1' key to Zoom 1 times
        # left_X = rescale_frame(left_crop, percent=200)
        # right_X = rescale_frame(right_crop, percent=200)
        # cv2.imshow('zoom leftX', left_X)
        # cv2.imshow('zoom rightX', right_X)
        X = 1
        print("Zoom in X1")

    elif k == ord('2'): # wait for '2' key to Zoom 2 time
        X = 2
        print("Zoom in X2")

    elif k == ord('3'): # wait for '3' key to Zoom 3 time
        X = 3
        print("Zoom in X3")

    elif k == ord('4'): # wait for '4' key to Zoom 4 time
        X = 4
        print("Zoom in X4")

    elif k == ord('5'): # wait for '5' key to Zoom 5 time
        X = 5
        print("Zoom in X5")

    cv2.imshow('Camera', raw_frame)
    # cv2.imshow('Video', frame)

    frame_zoom = rescale_frame(frame, percent=X*100)
    cv2.imshow('zoom frame', frame_zoom)

    H, W, Ch = frame_zoom.shape
    # H, W, Ch = raw_frame.shape

    H_half = H//2
    W_half = W//2

    # Zoom_crop = frame_zoom[W_half-150:W_half+150, H_half-200:H_half+200]
    Zoom_crop = frame_zoom[H_half-150:H_half+150, W_half-200:W_half+200]

    cv2.imshow('Zoom Resized', Zoom_crop)

    # cv2.namedWindow("window_C", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("window_C",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    # cv2.imshow("window_C", Zoom_crop)

    # outcrop.write(frame_zoom)         #I guess the problem lies in "(sky)" ?

cap.release()
# outcrop.release()
cv2.destroyAllWindows()