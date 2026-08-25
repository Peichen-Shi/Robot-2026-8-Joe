import os

for folder in [
    "./dataset/labels/train",
    "./dataset/aug_labels"
]:
    count0=0
    count1=0

    for f in os.listdir(folder):
        if f.endswith(".txt"):
            with open(os.path.join(folder,f)) as file:
                for line in file:
                    if line.startswith("0"):
                        count0+=1
                    elif line.startswith("1"):
                        count1+=1

    print(folder,count0,count1)