import cv2
from pathlib import Path

VIDEO_PATH = r"C:\Users\spc\Desktop\cup.mp4"
OUTPUT_DIR = Path(r"D:\studys\Pycharm\PycharmProjects\Robot-2026-8-Joe\Task 1\dataset\images\cup")

# 每秒抽取多少张
TARGET_FPS = 2

def extract_frames(video_path, output_dir, target_fps):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError("视频打开失败")

    original_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(
        cap.get(cv2.CAP_PROP_FRAME_COUNT)
    )
    # 原视频帧间隔
    frame_interval = round(
        original_fps / target_fps
    )
    print(f"原始FPS: {original_fps}")
    print(f"总帧数: {total_frames}")
    print(f"抽帧间隔: 每 {frame_interval} 帧取1帧")
    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )
    frame_id = 0
    save_id = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_id % frame_interval == 0:
            filename = (output_dir/f"cup_{save_id:04d}.jpg")
            cv2.imwrite(str(filename),frame)
            save_id += 1
        frame_id += 1

    cap.release()

    print(f"完成，共生成 {save_id} 张图片")


if __name__ == "__main__":
    extract_frames(VIDEO_PATH, OUTPUT_DIR, TARGET_FPS)
