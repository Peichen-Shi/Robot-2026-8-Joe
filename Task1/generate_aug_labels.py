import os
import shutil


AUG_IMAGE_DIR = "./dataset/aug_images"

LABEL_DIR = "./dataset/labels"

AUG_LABEL_DIR = "./dataset/aug_labels"


def main():

    os.makedirs(AUG_LABEL_DIR, exist_ok=True)

    count = 0

    for img in os.listdir(AUG_IMAGE_DIR):

        if not img.endswith((".jpg", ".png", ".jpeg")):
            continue


        # 例如:
        # cup_0000_aug_0.jpg
        # 截取:
        # cup_0000

        name = img.split("_aug")[0]


        label_path = None


        for cls in ["cup", "mouse"]:

            path = os.path.join(
                LABEL_DIR,
                cls,
                name + ".txt"
            )

            if os.path.exists(path):

                label_path = path
                break


        if label_path is None:

            print(
                "没有找到label:",
                img
            )

            continue


        new_label = os.path.join(
            AUG_LABEL_DIR,
            img.rsplit(".",1)[0]+".txt"
        )


        shutil.copy(
            label_path,
            new_label
        )


        count += 1


    print(
        "增强label生成完成:",
        count
    )


if __name__ == "__main__":
    main()