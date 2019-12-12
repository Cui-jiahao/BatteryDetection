# RetinaNet-Pytorch

## Describing

Pytorch  implementation of RetinaNet object detection as described in [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002) by Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He and Piotr Dollár.

This implementation is primarily designed to be easy to read and simple to modify.

## Installation

1) Clone this repo

2) Install the python packages:
```
pip install cffi

pip install pandas

pip install cython

pip install pycocotools

pip install opencv-python

pip install requests

```

## Eval测试

1) 下载的训练模型存放到weights文件夹中，百度网盘链接:

2) 执行下列命令
```
python eval.py -B battery_txt -A annotation -I image

```






