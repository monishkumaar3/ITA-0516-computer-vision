import cv2

video = cv2.VideoCapture("chahun main ya na short.mp4")

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow('Video in Reverse', frame)
    cv2.waitKey(30)

video.release()
cv2.destroyAllWindows()
