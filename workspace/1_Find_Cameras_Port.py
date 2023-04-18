import cv2

cams_test = 1000
for i in range(0, cams_test):
    cap = cv2.VideoCapture(i)
    test, frame = cap.read()
    print("i : "+str(i)+" /// result: "+str(test))


# i : 1 /// result: True
# i : 700 /// result: True
# i : 701 /// result: True
# i : 702 /// result: True