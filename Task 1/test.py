from ultralytics import YOLO
import cv2
import os


model = YOLO("./runs/detect/train-2/weights/best.pt")


img_dir = "./dataset/images/val"


images = [x for x in os.listdir(img_dir) if x.endswith((".jpg", ".png", ".jpeg"))]


for name in images:

    path = os.path.join(img_dir, name)

    img = cv2.imread(path)

    results = model(img, conf=0.5)

    result_img = results[0].plot()

    cv2.imshow("result", result_img)

    print("测试图片:", name)

    key = cv2.waitKey(0)

    # 按ESC退出
    if key == 27:
        break


cv2.destroyAllWindows()