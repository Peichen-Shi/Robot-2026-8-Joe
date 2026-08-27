import os

label_dir = r"D:\studys\Pycharm\PycharmProjects\Robot-2026-8-Joe\Task1\dataset_new\labels\train"

for file in os.listdir(label_dir):

    if file.startswith("mouse_add") and file.endswith(".txt"):

        path = os.path.join(label_dir,file)

        with open(path,"r") as f:
            lines=f.readlines()

        new_lines=[]

        for line in lines:
            parts=line.strip().split()

            if parts:
                # mouse类别改成1
                parts[0]="1"

            new_lines.append(" ".join(parts)+"\n")

        with open(path,"w") as f:
            f.writelines(new_lines)

print("mouse labels fixed")