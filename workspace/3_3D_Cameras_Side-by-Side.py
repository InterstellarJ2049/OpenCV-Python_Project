import numpy as np
import cv2
# import screeninfo
from screeninfo import get_monitors
# from screeninfo import get_monitors, Enumerator
import json

# the result is a Python dictionary:
# print(data["X2_left"])
# print(type(data["X2_left"]))

# parameter = {
#     "X2_left":10,
#     "X2_right":10,
#     "X3_left":10,
#     "X3_right":10,
#     "X4_left":10,
#     "X4_right":10,
#     "X5_left":10,
#     "X5_right":10,
# }

# with open('3D_CCM_parameter_data.json') as datas:
#     parameter = json.load(datas)
    
# for X2_left in parameter['zoom']['X2']['left']:
#     X2_left_int = int(X2_left)
#     print(X2_left_int)
#     print(type(X2_left_int))
    
# for X2_right in parameter['zoom']['X2']['right']:
#     X2_right_int = int(X2_right)
    
# for X3_left in parameter['zoom']['X3']['left']:
#     X3_left_int = int(X3_left)
    
# for X3_right in parameter['zoom']['X3']['right']:
#     X3_right_int = int(X3_right)
    
# print(X2_left_int)
# print(type(X2_left_int))

for M in get_monitors():
    print(str(M))

    # get the size of the screen
    screen = get_monitors()[1] # [0][1]...port number of display
    # print(screen)
    # width, height = screen.width, screen.height

cap_L = cv2.VideoCapture(0)
cap_R = cv2.VideoCapture(3)
# cap_L = cv2.VideoCapture(3) #2
# cap_R = cv2.VideoCapture(1)
# cap_L = cv2.VideoCapture(1)
# cap_R = cv2.VideoCapture(0)
# outcrop = cv2.VideoWriter('outcrop.mov', -1, 20.0, (640,480))

# times of zoom in
X = 1

# times of cropping size
# a = 20
a = 15

# shifting of cropping
i = 0
j = 0
m = 0
n = 0

# i = X2_left_int
# print(i)

# aspect ratio
h = 9
l = 16

# Offset
# horizonOffset = 50
# verticalOffset = -28

# Endoscope Objest Distance 3cm
# horizonOffset = -61
# verticalOffset = 4

# Endoscope Objest Distance 4cm
# horizonOffset = -49
# verticalOffset = 6

# Endoscope Objest Distance 5cm
# horizonOffset = -40
# verticalOffset = 5

horizonOffset = 0
verticalOffset = 0

# parameter =  '{ "X2_left":20, "X2_right":20, "X3_left":30, "X3_right":30, "X4_left":40, "X4_right":40, "X5_left":50, "X5_right":50}'
# parameter =  '{ "X2_left":5, "X2_right":5, "X3_left":5, "X3_right":5, "X4_left":5, "X4_right":5, "X5_left":5, "X5_right":5}'
parameter =  '{ "X2_left":0, "X2_right":0, "X3_left":0, "X3_right":0, "X4_left":0, "X4_right":0, "X5_left":0, "X5_right":0}'

# parse x:
data = json.loads(parameter)

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

def rescale_frame(frame, percent=100):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while True:
    ret, raw_frame_L = cap_L.read()
    ret, raw_frame_R = cap_R.read()
    # frame = raw_frame[100:200, 100:200]
    # raw_frame_R = cv2.rotate(raw_frame_R,cv2.ROTATE_180) # Right image rotate 180 degrees
    frame_L = raw_frame_L[:, :]
    frame_R = raw_frame_R[:, :]
    # sky = cv2.resize(sky, (640, 480))


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    elif k == ord('1'): # wait for '1' key to Zoom 1 times
        # left_X = rescale_frame(left_crop, percent=200)
        # right_X = rescale_frame(right_crop, percent=200)
        # cv2.imshow('zoom leftX', left_X)
        # cv2.imshow('zoom rightX', right_X)
        i = 0 # horizonOffset
        j = 0 # - horizonOffset
        m = 0 # verticalOffset
        n = 0 # - verticalOffset
        X = 1
        print("Zoom in X1")

    elif k == ord('2'): # wait for '2' key to Zoom 2 time
        X = 2
        # i = data["X2_left"]
        # j = 0 - data["X2_right"]
        i = horizonOffset * (X-1)
        j = 0 - horizonOffset * (X-1)
        m = 0 - verticalOffset * (X-1)
        n = verticalOffset * (X-1)
        # print(i)
        # with open('3D_CCM_parameter_data.json') as datas:
        #     parameter = json.load(datas)
    
        # for X2_left in parameter['zoom']['X2']['left']:
        #     X2_left_int = int(X2_left)
            
        # for X2_right in parameter['zoom']['X2']['right']:
        #     X2_right_int = int(X2_right)
        #     i = i + X2_left_int
        #     j = j - X2_right_int
        # i = X2_left_int
        # print(i)
        # print(j)
        # print(type(i))
        print("Zoom in X2")
                        
    elif k == ord('3'): # wait for '3' key to Zoom 3 time
        X = 3
        # i = data["X3_left"]
        # j = 0 - data["X3_right"]
        i = horizonOffset * (X-1)
        j = 0 - horizonOffset * (X-1)
        m = 0 - verticalOffset * (X-1)
        n = verticalOffset * (X-1)
        # i = i + X3_left_int
        # j = j + X3_right_int
        print("Zoom in X3")
                
    elif k == ord('4'): # wait for '4' key to Zoom 4 time
        X = 4
        # i = data["X4_left"]
        # j = 0 - data["X4_right"]
        i = horizonOffset * (X-1)
        j = 0 - horizonOffset * (X-1)
        m = 0 - verticalOffset * (X-1)
        n = verticalOffset * (X-1)
        print("Zoom in X4")

    elif k == ord('5'): # wait for '5' key to Zoom 5 time
        X = 5
        # i = data["X5_left"]
        # j = 0 - data["X5_right"]
        i = horizonOffset * (X-1)
        j = 0 - horizonOffset * (X-1)
        m = 0 - verticalOffset * (X-1)
        n = verticalOffset * (X-1)
        print("Zoom in X5")

    
    elif k == ord('a'): # wait for 'a' key to Move Cropping left
        i = i - 1
        print("Move Left-Cropping left")

    elif k == ord('d'): # wait for 'd' key to Move Cropping right
        i = i + 1
        print("Move Left-Cropping right")

    elif k == ord('j'): # wait for 'a' key to Move Cropping left
        j = j - 1
        print("Move Right-Cropping left")

    elif k == ord('l'): # wait for 'd' key to Move Cropping right
        j = j + 1
        print("Move Right-Cropping right")

    elif k == ord('w'): # wait for 'a' key to Move Cropping left
        m = m - 1
        print("Move Left-Cropping up")

    elif k == ord('s'): # wait for 'd' key to Move Cropping right
        m = m + 1
        print("Move Left-Cropping down")

    elif k == ord('i'): # wait for 'a' key to Move Cropping left
        n = n - 1
        print("Move Right-Cropping up")

    elif k == ord('k'): # wait for 'd' key to Move Cropping right
        n = n + 1
        print("Move Right-Cropping down")


    elif k == ord('<'): # wait for '<' key to change the times of cropping size
        a = a - 1
        print("Cropping Zoom out")

    elif k == ord('>'): # wait for '>' key to change the times of cropping size
        a = a + 1
        print("Cropping Zoom in")


    cv2.imshow('Camera_L', raw_frame_L)
    cv2.imshow('Camera_R', raw_frame_R)
    # cv2.imshow('Video', frame)

    frame_zoom_L = rescale_frame(frame_L, percent=X*100)
    frame_zoom_R = rescale_frame(frame_R, percent=X*100)
    # cv2.imshow('zoom frame', frame_zoom)

    H, W, Ch = frame_zoom_L.shape

    H_half = H//2
    W_half = W//2

    # 3840:2160 = 1920:1080 = 1280:720 = 16:9
    
    # Zoom_crop_L = frame_zoom_L[H_half-150:H_half+150, W_half-200:W_half+200]
    # Zoom_crop_R = frame_zoom_R[H_half-150:H_half+150, W_half-200:W_half+200]
    Zoom_crop_L = frame_zoom_L[H_half+verticalOffset-a*9-m:H_half+verticalOffset+a*9-m, W_half+horizonOffset-a*16+i:W_half+horizonOffset+a*16+i]
    Zoom_crop_R = frame_zoom_R[H_half-verticalOffset-a*9-n:H_half-verticalOffset+a*9-n, W_half-horizonOffset-a*16+j:W_half-horizonOffset+a*16+j]
    # Zoom_crop_L = frame_zoom_L[H_half-verticalOffset-a*9-m:H_half-verticalOffset+a*9-m, W_half-horizonOffset-a*16+i:W_half-horizonOffset+a*16+i]
    # Zoom_crop_R = frame_zoom_R[H_half+verticalOffset-a*9-n:H_half+verticalOffset+a*9-n, W_half+horizonOffset-a*16+j:W_half+horizonOffset+a*16+j]
    # Zoom_crop_L = frame_zoom_L[H_half-a*9-m:H_half+a*9-m, W_half-a*18+i:W_half+a*18+i]
    # Zoom_crop_R = frame_zoom_R[H_half-a*9-n:H_half+a*9-n, W_half-a*18+j:W_half+a*18+j]

    # left_crop = left_X[W3_half-a*9-m:W3_half+a*9-m, H3_half-a*9+i:H3_half+a*9+i]
    # right_crop = right_X[W3_half-a*9-n:W3_half+a*9-n, H3_half-a*9+j:H3_half+a*9+j]

    cv2.imshow('Zoom Resized_L', Zoom_crop_L)
    cv2.imshow('Zoom Resized_R', Zoom_crop_R)

    # setting mouse handler for the image
	# and calling the click_event() function
    cv2.setMouseCallback('Camera_L', click_event)
    cv2.setMouseCallback('Camera_R', click_event)
    cv2.setMouseCallback('Zoom Resized_L', click_event)
    cv2.setMouseCallback('Zoom Resized_R', click_event)

    # vis0 = np.concatenate((frame_zoom_L, frame_zoom_R), axis=1)
    # cv2.imshow('Combine', vis0)
    vis = np.concatenate((Zoom_crop_L, Zoom_crop_R), axis=1)
    cv2.imshow('Combine_Crop', vis)

    cv2.namedWindow("window_C", cv2.WND_PROP_FULLSCREEN)
    # cv2.moveWindow("window_C", 3840, 0)
    # cv2.moveWindow("window_C", screen.x + 3840, screen.y - 0)
    cv2.moveWindow("window_C", screen.x - 1, screen.y - 1)
    cv2.setWindowProperty("window_C",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    # cv2.imshow("window_C", vis0)
    cv2.imshow("window_C", vis)
    # cv2.moveWindow("window_C", 3840, 0)

    # outcrop.write(frame_zoom)         #I guess the problem lies in "(sky)" ?

cap_L.release()
cap_R.release()
# outcrop.release()
cv2.destroyAllWindows()