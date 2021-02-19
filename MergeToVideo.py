import cv2
import os
frame = cv2.imread('./01_0014/000.jpg')
#cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#_, frame = cap.read()
out = cv2.VideoWriter('output_white.avi', fourcc, 20, (frame.shape[1], frame.shape[0]))
#out = cv2.VideoWriter('output_white.avi', fourcc, 20, (frame.shape[1], frame.shape[0]), False) 用于灰度图
#这里，out是一个VideoWriter实例化对象，第一个参数是要制作的视频的文件名，20是fps，接下来是视频的长宽，如果要
#保存只有两维的灰度图，则最后还要加个False
frame_list = os.listdir('./01_0014')
for img in frame_list:
    frame = cv2.imread('./01_0014/'+img)
    out.write(frame)


out.release()
cv2.destroyAllWindows()