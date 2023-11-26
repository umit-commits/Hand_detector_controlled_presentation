import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

my_path = "slides" # input slides to add 
width, height = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
path_images = sorted(os.listdir(my_path)) # list of name of images
imgNumber = 3
hs, ws = 320,413
gestur_line = 300
button_press = False
button_counter = 0
button_delay = 20 # number of frames
#painting
annotations = [[]]
index_counter = 0
annotationFlag = False


# hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    path_full_image = os.path.join(my_path,path_images[imgNumber]) # os.path.join(name_of_folder, name of image in folder)
    current_image = cv2.imread(path_full_image) # imread function read it
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img,flipType=True)
    cv2.line(img,(0,gestur_line),(width,gestur_line),(0,255,0), 10)
    if hands and button_press == False: # if hands detectec -->
        hand = hands[0]
        fingers = detector.fingersUp(hand) # it will check how many finger is up
        # based on the this information, we will apply some gestures
        # but before applying some gestures, my fingers  should be above my face
        # so that my webcam wont misinterpret my gesture
        # if center point of my hand is above the gestur_line, then we accept the gesture
        cx,cy = hand['center']
        landmark_list = hand['lmList']
        # constrain values for easier drawing, we use np.interp
        index_finger = landmark_list[8][0], landmark_list[8][1]
        xval = int(np.interp(landmark_list[8][0], [width // 2,width], [0,width]))
        yval = int(np.interp(landmark_list[8][1], [150,height-150], [0, width]))
        # we are converting one range by another range
        index_finger = xval,yval

        if cy <= gestur_line: # if the face ath the height of the fac
            annotationFlag == False
            if fingers == [1,0,0,0,0]: # if we open up our thumb
                annotationFlag = False
                if(imgNumber > 0):
                    button_press = True
                    imgNumber -= 1
                    #####
                    annotations = [[]]
                    index_counter = 0


            if fingers == [0,0,0,0,1]:
                annotationFlag = False
                if(imgNumber < len(path_images) -1):
                    button_press = True
                    imgNumber += 1
                    #####
                    annotations = [[]]
                    index_counter = 0


        if fingers == [0,1,1,0,0]:
            cv2.circle(current_image,index_finger,12,(0,0,255),cv2.FILLED)
            #annotations = []
            # we will constraint the area of image so that we can easily move our pointer

        if fingers == [0,1,1,1,0]:
            if(annotations and index_counter >= -1):
                annotations.pop(-1)
                index_counter -= 1
                button_press = True
                annotationFlag = False


        # how to draw with our index finger
        if fingers == [0,1,0,0,0]:
            if annotationFlag == False:
                annotationFlag = True
                index_counter += 1
                annotations.append([])
            cv2.circle(current_image, index_finger, 12, (0, 0, 255), cv2.FILLED)
            annotations[index_counter].append(index_finger)

        else:
            annotationFlag = False

    else:
        annotationFlag =False
    #button_press_iteration
    if(button_press):
        button_counter += 1
        if(button_counter > button_delay):
            button_counter = 0
            button_press = False


    for i in range (len(annotations)):
        for j in range(len(annotations[i])):
            if(j != 0):
                cv2.line(current_image,annotations[i][j-1], annotations[i][j],(0,0,200),12)


    #adding webcam on slides
    imgSmall = cv2.resize(img,(ws,hs))
    h,w,_ = current_image.shape
    current_image[0:hs,w-ws:w] = imgSmall # we are about to insert our webcam to current_image

    cv2.imshow("Image",img)
    cv2.imshow("slide1", current_image)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
