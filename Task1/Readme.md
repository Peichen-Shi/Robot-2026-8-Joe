# 情况梳理
## 数据集
数据集有前后两部分。
### 第一部分
- 来源：手机拍摄的视频
- 处理：将视频拆分为图片帧，提取每一帧的图像数据。
- 数据量：十多张
- 预处理：数据增强，包括亮度，对比度等。不包括旋转、翻转等操作，因为涉及到label
- label: github上找的手动label的代码，基于opencv库
- 目标：这一阶段的主要目的是先把整个流程跑通：采集图片 → 标注 → 数据增强 → YOLO10训练 → best.pt → 导出ONNX → Jetson实时检测
- 问题：问题很明显，数据集中只有黑色的鼠标和绿色的杯子，导致模型效果很差，只能识别黑色鼠标和绿色杯子，其他颜色的鼠标和杯子无法识别，甚至会把黑色的键盘和显示器识别成鼠标。
### 第二部分
- 来源：
  - mouse: https://app.roboflow.com/login
  - cup: https://www.kaggle.com/datasets/andrewmvd/cup-detection
- 探索：

  为了减少模型把颜色、背景当成类别特征的问题，开始尝试公开数据集。 最先考虑了 COCO，因为 COCO 本身包含：

  - cup
  - computer mouse
  
  但完整 COCO 数据超过 10GB，对当前两分类任务明显过大，因此放弃全量 COCO。 随后转向：
  - Kaggle
  - Roboflow Universe
  
  这种规模更小、已经带 bbox 标注的数据集。
- 处理
  - 主要是将下载的数据集转换成yolo需要的结构，包括data.yaml,val,train,test等文件。 其中data.yaml中存放的是类别信息和数据集划分信息。
  - 这部分的代码在 split_yolo.py 中
  - 此外，由于不同的数据集对数据分类的id不同，需要对数据集进行统一的类别id映射。 这部分的代码在 label.py 中
  - 几百张数据对yolo足够，我选取了其中两百张及其label作为训练集
  - 数据量足够，无预处理
- label: 公开数据集自带bbox标注

## 模型，训练和测试
- 模型：github上找的yolov10，基于pytorch
- 训练：yolov10自带的train.py，主要是指定data.yaml。
  - 经实验，20/50 epoch loss未收敛。所以最终训练100 epoch
  - 基于 4070laptop，训练时间约为 30min
- 测试：yolov10自带的test.py
  - 测试集：从下载的两个数据集中各抽20张进行测试，显示准确率在90%以上
- 下载：源文件不带预训练的权重，需要下载
- 权重转换：onnx在边缘设备的推理速度更快，因此需要将yolov10训练得到的best.pt转换为onnx格式。 这部分的代码在 converge2jetson.py 中

## Git
- 代码托管：github
- 仓库：https://github.com/Peichen-Shi/Robot-2026-8-Joe

## Jetson
- 设备：Jetson Orin NX
- 系统：Ubuntu
- 运行环境：integration,是学长留下来的、经过配置的conda环境，可直接使用
- 部署：
  - 将yolov10训练得到的best.pt转换为onnx格式
  - 将onnx模型通过ssh传输到Jetson上
  - 在Jetson上找到摄像头设备，并通过代码调用摄像头进行实时检测
- 在 Jetson上建立了自己的项目 PeichenShi，保证与其他组员的项目独立
