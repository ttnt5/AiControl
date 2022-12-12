import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
import serial
import time
import math

arduino = serial.Serial('com3', 9600)
time.sleep(1)
action1 =''
d1 = 0
actions = ['0s', '90s', '180s']
seq_length = 30

model = load_model('models/model.h5')

# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
seq = []
action_seq = []

while cap.isOpened():
    ret, img = cap.read()
    img0 = img.copy()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks is not None:
        for res in result.multi_hand_landmarks:
            joint = np.zeros((21, 4))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

            # Compute angles between joints
            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19], :3] # Parent joint
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], :3] # Child joint
            v = v2 - v1 # [20, 3]
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

            # Get angle using arcos of dot product
            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

            angle = np.degrees(angle) # Convert radian to degree

            d = np.concatenate([joint.flatten(), angle])

            seq.append(d)

            mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

            if len(seq) < seq_length:
                continue

            input_data = np.expand_dims(np.array(seq[-seq_length:], dtype=np.float32), axis=0)

            y_pred = model.predict(input_data).squeeze()

            i_pred = int(np.argmax(y_pred))
            conf = y_pred[i_pred]

            if conf < 0.9:
                continue

            action = actions[i_pred]
            action_seq.append(action)

            if len(action_seq) < 3:
                continue

            # this_action = '?'
            # if action_seq[-1] == action_seq[-2] == action_seq[-3]:
            #     this_action = action
            

            for hand_landmarks in result.multi_hand_landmarks:
                h, w, c = img.shape
                x1 = int(hand_landmarks.landmark[5].x * w)
                y1 = int(hand_landmarks.landmark[5].y * h)

                x2 = int(hand_landmarks.landmark[8].x * w)
                y2 = int(hand_landmarks.landmark[8].y * h)

                radian = math.atan2(y2 - y1, x2 - x1)
                degree = int(radian * 180 / math.pi + 180)
                print(degree)
            if action == '90s'  and 110 >= degree >= 70:
                action1 = '90s'
            if action == ('180s' or '0s')  and 200 >= degree >= 160:
                action1 = '180s'
            if action == ('0s' or '180s')  and (340 <= degree <= 360 or 0 <= degree <= 20):
                action1 = '0s'

            print(action1)

            cv2.putText(img, f'{action1.upper()}', org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)
            action1= str(action1)
            
            if action1 =='90s':
                d1 = '2'
            if action1 == '180s':
                d1 = '3'
            if action1 == '0s':
                d1 = '1'

            d1 = d1.encode('utf-8')
            arduino.write(d1)

    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break