import os
import random
import shutil


IMAGE_DIR = "./dataset/images"

LABEL_DIR = "./dataset/labels"


AUG_IMAGE_DIR = "./dataset/aug_images"

AUG_LABEL_DIR = "./dataset/aug_labels"


OUT_IMAGE_DIR = "./dataset/images"

OUT_LABEL_DIR = "./dataset/labels"


VAL_RATIO = 0.2



def clear_old():

    paths = [

        "./dataset/images/train",
        "./dataset/images/val",

        "./dataset/labels/train",
        "./dataset/labels/val"

    ]


    for path in paths:

        if os.path.exists(path):

            shutil.rmtree(path)



def get_original_data():

    data = []


    for cls in ["cup","mouse"]:


        img_dir = os.path.join(
            IMAGE_DIR,
            cls
        )


        label_dir = os.path.join(
            LABEL_DIR,
            cls
        )


        for img in os.listdir(img_dir):

            if img.endswith(
                (".jpg",".png",".jpeg")
            ):


                label = img.rsplit(".",1)[0]+".txt"


                img_path = os.path.join(
                    img_dir,
                    img
                )


                label_path = os.path.join(
                    label_dir,
                    label
                )


                if os.path.exists(label_path):

                    data.append(
                        (
                            img_path,
                            label_path
                        )
                    )


    return data



def get_aug_data():

    data = []


    for img in os.listdir(AUG_IMAGE_DIR):

        if img.endswith(
            (".jpg",".png",".jpeg")
        ):


            img_path = os.path.join(
                AUG_IMAGE_DIR,
                img
            )


            label_path = os.path.join(
                AUG_LABEL_DIR,
                img.rsplit(".",1)[0]+".txt"
            )


            if os.path.exists(label_path):

                data.append(
                    (
                        img_path,
                        label_path
                    )
                )


    return data



def copy_data(data,split):


    img_out = os.path.join(
        OUT_IMAGE_DIR,
        split
    )


    label_out = os.path.join(
        OUT_LABEL_DIR,
        split
    )


    os.makedirs(
        img_out,
        exist_ok=True
    )


    os.makedirs(
        label_out,
        exist_ok=True
    )


    for img,label in data:


        shutil.copy(
            img,
            os.path.join(
                img_out,
                os.path.basename(img)
            )
        )


        shutil.copy(
            label,
            os.path.join(
                label_out,
                os.path.basename(label)
            )
        )


    print(
        split,
        "完成:",
        len(data)
    )



def main():


    print("清理旧train/val")

    clear_old()


    original = get_original_data()

    augmented = get_aug_data()


    print(
        "原始图片:",
        len(original)
    )


    print(
        "增强图片:",
        len(augmented)
    )


    random.shuffle(original)


    val_num = int(
        len(original)*VAL_RATIO
    )


    val_data = original[:val_num]


    train_data = original[val_num:]


    # 增强全部进入训练集

    train_data += augmented


    random.shuffle(train_data)



    copy_data(
        train_data,
        "train"
    )


    copy_data(
        val_data,
        "val"
    )



if __name__ == "__main__":
    main()