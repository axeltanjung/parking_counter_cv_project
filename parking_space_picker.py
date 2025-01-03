import cv2
import pickle



cv2.imread('carParkImg.img')

width, height = 107, 48

try:
    with open('car_park_pos', 'wb') as f:
        posList = pickle.load(f)
except:
    posList = []

posList = []

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    if event == cv2.EVENT_RBUTTONDOWN:
        for pos in posList:
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
                break
    


while True:
    # cv2.rectangle(img, (50,192), (157, 240),(255, 0 255), 2)
    cv2.imread('carParkImg.img')

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow('image', img)
    cv2.setMouseCallback("Image", mouse_click)
    cv2.waitKey(1)