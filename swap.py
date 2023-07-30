import cv2
pic1=cv2.imread("kohli.jpeg.jpg")
pic3=cv2.imread("babar.png")
pic3[100:280,220:370]=pic1[120:300,200:350]
cv2.imshow("my photo",pic3)
cv2.waitKey()
cv2.destroyAllWindows()
