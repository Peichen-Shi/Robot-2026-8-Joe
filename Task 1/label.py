# -*- coding: utf-8 -*-

import cv2
import os

IMAGE_DIR = r"D:\studys\Pycharm\PycharmProjects\Robot-2026-8-Joe\Task 1\dataset\images\mouse"
LABEL_DIR = r"dataset/labels/cup"

CLASS_ID = 0   # mouse类别q

os.makedirs(LABEL_DIR, exist_ok=True)
drawing = False
ix, iy = -1, -1
box = None
def mouse_callback(event, x, y, flags, param):
    global ix, iy, drawing, box

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            box = (ix, iy, x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        box = (ix, iy, x, y)


def save_label(img_path, box, img_shape):
    h, w = img_shape[:2]

    x1, y1, x2, y2 = box

    x_min = min(x1, x2)
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    y_max = max(y1, y2)

    # YOLO格式
    x_center = ((x_min + x_max) / 2) / w
    y_center = ((y_min + y_max) / 2) / h

    box_w = (x_max - x_min) / w
    box_h = (y_max - y_min) / h

    name = os.path.splitext(os.path.basename(img_path))[0]

    label_path = os.path.join(LABEL_DIR, name + ".txt")

    with open(label_path, "w") as f:
        f.write(f"{CLASS_ID} {x_center:.6f} {y_center:.6f} {box_w:.6f} {box_h:.6f}")

    print("保存:", label_path)

images = [
    x for x in os.listdir(IMAGE_DIR)
    if x.endswith((".jpg", ".png", ".jpeg"))
]
images.sort()

index = 0

while index < len(images):

    img_path = os.path.join(
        IMAGE_DIR,
        images[index]
    )
    img = cv2.imread(img_path)

    display = img.copy()
    box = None
    cv2.namedWindow("label")
    cv2.setMouseCallback("label", mouse_callback)
    while True:

        temp = display.copy()

        if box:
            cv2.rectangle(
                temp,
                (box[0], box[1]),
                (box[2], box[3]),
                (0,255,0),
                2
            )

        cv2.imshow(
            "label",
            temp
        )

        key = cv2.waitKey(20)


        # 保存
        if key == ord("s"):

            if box:
                save_label(
                    img_path,
                    box,
                    img.shape
                )

            break


        # 下一张
        if key == ord("n"):
            break
        # 退出
        if key == ord("q"):
            exit()
    index += 1
cv2.destroyAllWindows()