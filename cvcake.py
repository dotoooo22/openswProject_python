import cv2
from tkinter import *
from tkinter.colorchooser import *
from PIL import Image, ImageTk
import numpy as np

clickflag = 0       # 클릭상태 확인 전역변수 초기값 0
global r,g,b
global w
##img = cv2.imread('C:/cakeImage/cakebase3.png', cv2.IMREAD_COLOR)          # img에 이미지를 불러옴.
font = cv2.FONT_HERSHEY_DUPLEX                                                      # 텍스트의 폰트를 지정.
img1 = cv2.imread('C:/cakeImage/whip2.png', 1)
img = cv2.imread('C:/cakeImage/cakebase3.png', 1)

def nothing(x):
    pass

# def draw_circle(event, x, y,flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN :
#         cv2.circle(img, (x, y),1, (r,g,b),w ,-1)

def free_drawing(event, x,y, flags, param):
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    w = cv2.getTrackbarPos('weight', 'image')
    global clickflag
    if event == cv2.EVENT_LBUTTONDOWN:
        clickflag = 1
    if event == cv2.EVENT_LBUTTONUP:
        clickflag = 0
    if event == cv2.EVENT_MBUTTONDOWN:
        clickflag = 2
    if event == cv2.EVENT_MBUTTONUP:
        clickflag = 0
    if event == cv2.EVENT_RBUTTONDOWN:
        clickflag = 3
    if event == cv2.EVENT_RBUTTONUP:
        clickflag = 0
    if clickflag == 1:
        event = cv2.EVENT_MOUSEMOVE  # 플레그가 1일때, 마우스가 움직여도 그림이 그려짐
        cv2.circle(img, (x, y), w, (b, g, r), -1)
    if clickflag == 2:
        event = cv2.EVENT_MOUSEMOVE
        cv2.circle(img, (x, y), w, (255, 255, 255), -1)
    if clickflag == 3:
        get_image(x, y)

def get_image(x, y):
    h, w, c = img1.shape
    roi = img[y:y+h, x:x+w]  # 배경이미지의 변경할(다음 로고 넣을) 영역
    mask = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 로고를 흑백처리
    # 이미지 이진화 => 배경은 검정. 글자는 흰색
    mask[mask[:] == 255] = 0
    mask[mask[:] > 0] = 255
    mask_inv = cv2.bitwise_not(mask)  # mask반전.  => 배경은 흰색. 글자는 검정
    daum = cv2.bitwise_and(img1, img1, mask=mask)  # 마스크와 로고 칼라이미지 and하면 글자만 추출됨
    back = cv2.bitwise_and(roi, roi, mask=mask_inv)  # roi와 mask_inv와 and하면 roi에 글자모양만 검정색으로 됨
    dst = cv2.add(daum, back)  # 로고 글자와 글자모양이 뚤린 배경을 합침
    img[y:y+h, x:x+w] = dst  # roi를 제자리에 넣음
    
def drawcake():
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', free_drawing)         #  free_drawing 함수 호출 (이곳에서 윈도우에서 실행결정)
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)
    cv2.createTrackbar('weight', 'image', 5, 30, nothing)
    cv2.putText(img, 'Hello World', (110, 240), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    
    while(1):
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 0x1B:                  # 무한 반복중, 키보드 ESC 아스키코드가 들어오면 빠져나감.
            break
         
        
        # s = cv2.getTrackbarPos('switch', 'image')
        
    cv2.destroyAllWindows()
    