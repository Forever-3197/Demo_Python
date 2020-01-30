#import os

#cur_path = os.path.dirname(os.path.realpath(__file__))
#os.putenv("PYTHONPATH", cur_path)

#导入cv模块
import cv2
import tensorflow as tf

print(tf.__version__)
print(tf.__path__)

#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv2.imread("./gril.jpg")
#创建窗口并显示图像
cv2.namedWindow("Image")
cv2.imshow("Image",img)
cv2.waitKeyEx()
#释放窗口
cv2.destroyAllWindows()


#from PIL import Image
#import matplotlib.pyplot as plt
#pil_im = Image.open('1.jpg')
#pil_im = Image.open('1.jpg').convert('L') #灰度操作
 
#plt.figure("dog")
#plt.imshow(pil_im)
#plt.show()