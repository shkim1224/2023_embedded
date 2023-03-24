import cv2
import mediapipe
import pyautogui
capture_hands = mediapipe.solutions.hands.Hands() # 
drawing_option = mediapipe.solutions.drawing_utils  # 너무 기니까 drawing_option 으로 간략화 시킴

camera = cv2.VideoCapture(0)
while True:
    _,image = camera.read()
    image = cv2.flip(image,1)
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    cv2.imshow("Hand movement video caputre", image)
    all_hands = output_hands.multi_hand_landmarks  # capture_hands 객체에 있는 데이터(multi_hand_landmarks)
    if all_hands:   # output_hands 객체에서 검출된 손이 있다면 
        for hand in all_hands:    # 각각을 찾아서 hand 라는 변수에 저장
            drawing_option.draw_landmarks(image, hand)
        
    key = cv2.waitKey(100)
    if key == 27:
        break
    
camera.release()
cv2.destroyAllWindows()   