from ultralytics import YOLO
import cv2


model = YOLO("./runs/detect/train/weights/best.pt")


img = cv2.imread("./dataset/images/val/test.jpg")


results = model(img)


for r in results:
    img = r.plot()


cv2.imshow("result", img)
cv2.waitKey(0)

cv2.destroyAllWindows()