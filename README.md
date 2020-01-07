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

## Testing

1) Download the training model and store it in the weights folder,the link address is:

2) Please run the script:
```
python eval.py -B battery_txt -A annotation -I image

```






