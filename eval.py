import numpy as np
import torchvision
import time
import os
import copy
import pdb
import time
import argparse

import sys
import cv2

import torch
from torch.utils.data import Dataset, DataLoader
from dataloader import CocoDataset, CSVDataset, collater, Resizer, AspectRatioBasedSampler, Augmenter, UnNormalizer, Normalizer,TXTDataset
from torchvision import datasets, models, transforms
import argparse
import csv_eval

ap     = argparse.ArgumentParser(description='Just for eval.')
ap.add_argument('-B','--ImageNamePath')
ap.add_argument('-A','--AnnotationPath')
ap.add_argument('-I','--ImagePath')
args = vars(ap.parse_args())

dataset_val = TXTDataset(ImgNamePth=args['ImageNamePath'], AnnoPth=args['AnnotationPath'], ImgPth =args['ImagePath'], transform=transforms.Compose([Normalizer(), Resizer()]))
sampler_val = AspectRatioBasedSampler(dataset_val, batch_size=1, drop_last=False)
dataloader_val = DataLoader(dataset_val, num_workers=3, collate_fn=collater, batch_sampler=sampler_val)
modelpath = os.path.join(os.path.dirname(__file__), 'weights/model.pt')
modelretina = torch.load(modelpath)
modelretina.cuda()
modelretina.eval()
AP = csv_eval.evaluate(dataset_val, modelretina)
map = (AP[0][0]+AP[1][0])/2
print("mAp:"+str(map))