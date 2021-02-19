import cv2
import argparse
import os

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '--video', help='input the path of the video')
parser.add_argument('-d', '--directory', help='input the saving path of the frames')
parser.add_argument('--show', action='store_true', help='turn to show the video')

opt = parser.parse_args()

cap = cv2.VideoCapture(opt.video)
os.makedirs(opt.directory, exist_ok=True)

i = 0
while(1):
    ret, frame = cap.read()
    try:
        cv2.imwrite('./images/'+str(i)+'.jpg', frame)
    except:
        break
    i = i + 1
    if opt.show:
        cv2.imshow("capture", frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows() 