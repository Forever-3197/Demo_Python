import cv2
import numpy as np
img = cv2.imread('./1.jpg', cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey(0)


#from PIL import Image
#import matplotlib.pyplot as plt
#pil_im = Image.open('1.jpg')
#pil_im = Image.open('1.jpg').convert('L') #灰度操作
 
#plt.figure("dog")
#plt.imshow(pil_im)
#plt.show()