import cv2
import numpy as np


img = cv2.imread('./images/0.jpg')
img = img[:, :, 0] # 获取rgb通道中的一个
print(img.shape)
img = np.float32(img) # 将数值精度调整为32位浮点型
img_dct = cv2.dct(img)  # 使用dct获得img的频域图像      
cv2.imwrite('dct_fake.jpg', img_dct) 
print(img_dct.shape)
img_recor2 = cv2.idct(img_dct)