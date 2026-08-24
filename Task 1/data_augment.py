# -*- coding: utf-8 -*-

"""
无label图片数据增强
增强方式:
1. 随机亮度/对比度
2. 高斯模糊
"""

import os
import random
from PIL import Image, ImageEnhance, ImageFilter
INPUT_DIR = r"images"
OUTPUT_DIR = r"./aug_images"
# 每张图片生成数量
AUG_NUM = 5

def augment_image(img):
    # 随机亮度
    img = ImageEnhance.Brightness(img).enhance(random.uniform(0.8, 1.2))

    # 随机对比度
    img = ImageEnhance.Contrast(img).enhance(random.uniform(0.8, 1.2))
    # 随机模糊
    if random.random() < 0.5:
        img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.5, 1.5)))
    return img


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    images = [x for x in os.listdir(INPUT_DIR) if x.endswith((".jpg", ".png", ".jpeg"))]
    print(f"发现 {len(images)} 张图片")
    count = 0

    for img_name in images:
        img_path = os.path.join(INPUT_DIR, img_name)
        img = Image.open(img_path).convert("RGB")
        for i in range(AUG_NUM):
            aug_img = augment_image(img.copy())
            save_name = img_name.rsplit(".", 1)[0] + f"_aug_{i}.jpg"
            aug_img.save(os.path.join(OUTPUT_DIR, save_name))
            count += 1

    print(f"增强完成，共生成 {count} 张图片")

if __name__ == "__main__":
    main()