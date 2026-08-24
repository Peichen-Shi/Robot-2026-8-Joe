from ultralytics import YOLO

model = YOLO(
    r"/Task1\runs\detect\train-2\weights\best.pt"
)

model.export(
    format="onnx",
    imgsz=640
)