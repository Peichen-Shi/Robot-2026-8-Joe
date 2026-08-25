from ultralytics import YOLO

# 1. 加载训练好的最佳模型
model = YOLO("./runs/detect/train/weights/best.pt")


# 2. 在验证集上评估
results = model.val(
    data="./dataset/data.yaml",
    split="val",
    imgsz=640,
    batch=16,
    device=0,
    workers=0
)


# 3. 输出指标
print("\n===== Validation Result =====")

print("mAP50:", results.box.map50)
print("mAP50-95:", results.box.map)

print("\nPer class:")
for i, name in model.names.items():
    print(
        name,
        "Precision:",
        results.box.p[i],
        "Recall:",
        results.box.r[i]
    )