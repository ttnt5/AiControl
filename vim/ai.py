import cv2
import mediapipe as mp
import numpy as np
mp_hands = mp.solutions.hands

#mp_drawing = mp.solutions.drawing_utils
#mp_drawing_styles = mp.solutions.drawing_styles

# 웹캠
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("카메라를 찾을 수 없습니다.")
      # 동영상을 불러올 경우는 'continue' 대신 'break'
      continue

    # 필요에 따라 성능 향상을 위해 이미지 작성을 불가능함으로 기본 설정합니다.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # 이미지에 손 주석을 그립니다.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:

        h,w,c = image.shape
        
        시작마디x, 시작마디y = int(hand_landmarks.landmark[5].x*w), int(hand_landmarks.landmark[5].y*h)
        끝마디x, 끝마디y = int(hand_landmarks.landmark[6].x*w), int(hand_landmarks.landmark[6].y*h)
        
        #radian=np.arctan2(시작마디y-끝마디y, 시작마디x-끝마디x)
        radian=np.arctan2(시작마디x-끝마디x, 시작마디y-끝마디y)
        #radian=np.arctan2(끝마디y-시작마디y, 끝마디x-시작마디x)
        #radian=np.arctan2(끝마디x-시작마디x, 끝마디y-시작마디y)
        degree = int(radian * 180 / np.pi)
        if degree < 0:
          degree=degree+360

        print(degree)

        #손가락 마디 그림
        # mp_drawing.draw_landmarks(
        #     image,
        #     hand_landmarks,
        #     mp_hands.HAND_CONNECTIONS,
        #     mp_drawing_styles.get_default_hand_landmarks_style(),
        #     mp_drawing_styles.get_default_hand_connections_style())

    cv2.imshow('손 인식', cv2.flip(image, 1))
    #cv2.imshow('손 인식', image)

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()