import cv2
video=cv2.VideoCapture('C:/Users/kravi/OneDrive/Desktop/Nature.mp4')

fourcc=cv2.VideoWriter_fourcc(*'mp4v')
output=cv2.VideoWriter('Output.mp4',fourcc,20.0,(500,500))

while video.isOpened():
    ret,frame=video.read()
    if ret:
        output.write(frame)
        cv2.imshow('Frame',frame)

        if cv2.waitKey(10) == ord('s'):
            break
    else:
        break
cv2.destroyAllWindows()