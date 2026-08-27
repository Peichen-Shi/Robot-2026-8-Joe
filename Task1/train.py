from ultralytics import YOLO


# 加载预训练YOLOv10模型
model = YOLO("./yolov10/yolov10n.pt")


# 开始训练
model.train(
    data="./dataset_new/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    device=0,
    workers=0
)


print("训练完成")