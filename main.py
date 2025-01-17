import cv2
import pickle
import cvzone
import numpy as np

# Video feed
cap = cv2.VideoCapture('./videos/carPark.mp4')

with open('car_park_pos', 'wb') as f:
    posList = pickle.load(f)

width, height = 107, 48

def check_parking_space(img_processed):

    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCropped = img[y:y + height, x:x + width]
        #cv2.imshow(str(x+y), imgCropped)
        count = cv2.countNonZero(imgCrop)
        

        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
        cvzone.putTextRect(img, str(count), (x, y+height-3), scale=0.1, 
                           thickness=2, offset=0, colorR = color)
    
    cvzone.putTextRect(img, f'Free: {str(spaceCounter)/{len(pos)}}', (100, 50), scale=3, 
                        thickness=5, offset=20, colorR = (0, 200, 0))

while True:

    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                         cv2.THRESH_BINARY, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones(3,3, np.uint8)
    imDilated = cv2.dilate(imgMedian, kernel, iterations1)
    
    check_parking_space()

    
    cv2.imshow("Image", img)
    cv2.waitKey(10)