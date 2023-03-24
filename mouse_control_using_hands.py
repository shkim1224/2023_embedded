import cv2
import mediapipe
import pyautogui
capture_hands = mediapipe.solutions.hands.Hands() # 
drawing_option = mediapipe.solutions.drawing_utils

camera = cv2.VideoCapture(0)
while True:
    _,image = camera.read()
    cv2.imshow("Hand movement video caputre", image)
    key = cv2.waitKey(100)
    if key == 27:
        break
    
camera.release()
cv2.destroyAllWindows()    