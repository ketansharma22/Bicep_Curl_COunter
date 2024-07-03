import  cv2
import cvzone
from cvzone.PoseModule import  PoseDetector
import  numpy as np
cap=cv2.VideoCapture(0)
detector=PoseDetector(detectionCon=0.69)
color=(0,0,255)
dir=0
curl_count=0
while True:
    _,img=cap.read()
    img=detector.findPose(img)
    lmlst, bbox= detector.findPosition(img,draw=False)

    if lmlst:
        # print(lmlst)
        angle=detector.findAngle(img,16,14,12)
        bar_val=np.interp(angle,(40,155),(60,300+60))
        per_val=np.interp(angle,(40,155),(100,0))
        cv2.rectangle(img,(560,int(bar_val)),(40+560,300+60),(color),cv2.FILLED)
        cv2.rectangle(img,(560,60),(40+560,300+60),(0,0,0),9)
        cvzone.putTextRect(img,f"{int(per_val)} %",(530,40),1.6,2,(255,255,255),color,border=4,colorB=())
        if per_val==100:
            if dir == 0:
                curl_count+=0.5
                dir=1
                color=(0,255,0)
        elif per_val==0:
            if dir == 1:
                curl_count+=0.5
                dir=0
                color=(0,255,0)
        else:
            color = (0, 0, 255)

    cvzone.putTextRect(img,"Bicep_Curl_Counter !!",(100,90),2,3,(255,255,255),(255,0,0),border=4,colorB=())
    cvzone.putTextRect(img, f'Curl Counter:{int(curl_count)}', (50, 150), 2, 3, (255, 255, 255), (0, 155, 0), border=4, colorB=())
    cv2.imshow("bicep curl counter",img)
    if cv2.waitKey(1) == ord("q"):
        break

        #50,150