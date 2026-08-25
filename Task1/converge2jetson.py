from ultralytics import YOLO

model = YOLO(
    r"runs/detect/train/weights/best.pt"
)

model.export(
    format="onnx",
    imgsz=640
)