import pyautogui
import cv2
import numpy as np
import pytesseract

def drawRectangle(event,x,y,flags,param):
    global ix,iy,drawing
    global roi
    drawing = False
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            drawing = False
            cv2.rectangle(readIn, (ix,iy), (x,y), (0,255,0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        cv2.rectangle(readIn, (ix,iy), (x,y), (0,255,0), 2)   
        refPoint = [(ix,iy), (x,y)]
        if len(refPoint) == 2:
            roi = readInCopy[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)

def readCharacter(inImg):
    text = pytesseract.image_to_string(inImg)
    return text


pyautogui.screenshot().save("D:/abc.png")
readIn = cv2.imread("D:/abc.png")
readInCopy = readIn.copy()
cv2.namedWindow("Crop", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Crop", drawRectangle)
cv2.imshow("Crop", readIn)
while(1):
    cv2.namedWindow('Crop',cv2.WINDOW_NORMAL)
    cv2.imshow('Crop',readIn)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if len(roi.shape) == 3:
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
roi = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(readCharacter(roi))







