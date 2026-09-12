import cv2
img=cv2.imread("C:/Users/kravi/OneDrive/Desktop/Highway.jpg",0)
print("Dimensions of the image:", img.shape)
width=400
height=400
dim=(width,height)
resized=cv2.resize(img,dim)
cv2.imshow("window",img.shape)
cv2.imwrite('/Users/kravi/OneDrive/Desktopcar.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()