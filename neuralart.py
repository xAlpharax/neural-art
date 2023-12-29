#!/bin/python

### imports (should be covered by requirements.txt)

from torch.autograd import Variable
from torchvision import transforms
from torch import optim

import torch.nn as nn
import torch.nn.functional as F

import torchvision
import torch

import time
import sys
import os

from collections import OrderedDict

import matplotlib.pyplot as plt

from PIL import Image

### path definitions

model_path = 'weights/vgg_conv_weights.pth'
image_path = '' # by default use neural-art as relative dir

### userland testing for multiple instances, a big nono currently

n_instances = os.popen('ps aux | grep "python neuralart.py" | wc -l').read() # TODO: add windows commands for platform compatibility :p for the 3 people who need this warning
if int(n_instances) > 3: print("Woah, running 2 or more instances of neural-art at the same time?\nThis is an experimental feature as of now... try it later :3")

### check if there are any weights to use, if not, download the default provided ones
if int(os.popen('ls -l weights | wc -l').read()) == 1: os.system(f'curl https://files.catbox.moe/wcao20.pth --output {model_path}') # TODO: win commands here as well

### Defining neural architecture

### VGG was trained on IMAGENET
### although old at this point
### it still achieves good results

class VGG(nn.Module):
    def __init__(self, pool='max'):
        super(VGG, self).__init__()

        self.conv1_1 = nn.Conv2d(3, 64, kernel_size = 3, padding = 1)
        self.conv1_2 = nn.Conv2d(64, 64, kernel_size = 3, padding = 1)

        self.conv2_1 = nn.Conv2d(64, 128, kernel_size = 3, padding = 1)
        self.conv2_2 = nn.Conv2d(128, 128, kernel_size = 3, padding = 1)

        self.conv3_1 = nn.Conv2d(128, 256, kernel_size = 3, padding = 1)
        self.conv3_2 = nn.Conv2d(256, 256, kernel_size = 3, padding = 1)
        self.conv3_3 = nn.Conv2d(256, 256, kernel_size = 3, padding = 1)
        self.conv3_4 = nn.Conv2d(256, 256, kernel_size = 3, padding = 1)

        self.conv4_1 = nn.Conv2d(256, 512, kernel_size = 3, padding = 1)
        self.conv4_2 = nn.Conv2d(512, 512, kernel_size = 3, padding = 1)
        self.conv4_3 = nn.Conv2d(512, 512, kernel_size = 3, padding = 1)
        self.conv4_4 = nn.Conv2d(512, 512, kernel_size = 3, padding = 1)

        self.conv5_1 = nn.Conv2d(512, 512, kernel_size = 3, padding = 1)
        self.conv5_2 = nn.Conv2d(512, 512, kernel_size = 3, padding = 1)
        self.conv5_3 = nn.Conv2d(512, 512, kernel_size = 3, padding = 1)
        self.conv5_4 = nn.Conv2d(512, 512, kernel_size = 3, padding = 1)

        # POOLING OPTIONS
        if pool == 'max':
            self.pool1 = nn.MaxPool2d(kernel_size = 2, stride = 2)
            self.pool2 = nn.MaxPool2d(kernel_size = 2, stride = 2)
            self.pool3 = nn.MaxPool2d(kernel_size = 2, stride = 2)
            self.pool4 = nn.MaxPool2d(kernel_size = 2, stride = 2)
            self.pool5 = nn.MaxPool2d(kernel_size = 2, stride = 2)

        elif pool == 'avg':
            self.pool1 = nn.AvgPool2d(kernel_size = 2, stride = 2)
            self.pool2 = nn.AvgPool2d(kernel_size = 2, stride = 2)
            self.pool3 = nn.AvgPool2d(kernel_size = 2, stride = 2)
            self.pool4 = nn.AvgPool2d(kernel_size = 2, stride = 2)
            self.pool5 = nn.AvgPool2d(kernel_size = 2, stride = 2)

    def forward(self, x, out_keys):
        out = {}

        out['r11'] = F.relu(self.conv1_1(x))
        out['r12'] = F.relu(self.conv1_2(out['r11']))
        out['p1'] = self.pool1(out['r12'])

        out['r21'] = F.relu(self.conv2_1(out['p1']))
        out['r22'] = F.relu(self.conv2_2(out['r21']))
        out['p2'] = self.pool2(out['r22'])

        out['r31'] = F.relu(self.conv3_1(out['p2']))
        out['r32'] = F.relu(self.conv3_2(out['r31']))
        out['r33'] = F.relu(self.conv3_3(out['r32']))
        out['r34'] = F.relu(self.conv3_4(out['r33']))
        out['p3'] = self.pool3(out['r34'])

        out['r41'] = F.relu(self.conv4_1(out['p3']))
        out['r42'] = F.relu(self.conv4_2(out['r41']))
        out['r43'] = F.relu(self.conv4_3(out['r42']))
        out['r44'] = F.relu(self.conv4_4(out['r43']))
        out['p4'] = self.pool4(out['r44'])

        out['r51'] = F.relu(self.conv5_1(out['p4']))
        out['r52'] = F.relu(self.conv5_2(out['r51']))
        out['r53'] = F.relu(self.conv5_3(out['r52']))
        out['r54'] = F.relu(self.conv5_4(out['r53']))
        out['p5'] = self.pool5(out['r54'])

        # RETURN DESIRED ACTIVATIONS
        return [out[key] for key in out_keys]



### COMPUTING GRAM MATRIX AND GRAM MATRIX LOSS

# GRAM MATRICES ARE USED TO MEASURE STYLE LOSS
class GramMatrix(nn.Module):

    def forward(self, input):
        b, c, w, h = input.size()
        F = input.view(b, c, h * w)

        # COMPUTES GRAM MATRIX BY MULTIPLYING INPUT BY TRANPOSE OF ITSELF
        G = torch.bmm(F, F.transpose(1, 2))
        G.div_(h*w)

        return G

class GramMSELoss(nn.Module):

    def forward(self, input, target):
        out = nn.MSELoss()(GramMatrix()(input), target)

        return out



### IMAGE PROCESSING

# "based" on how much vram you have,
# you can either set this to 1080
# as in 1080p or do what i did:
# set the resolution to 720p, and cry.

img_size = 720

# PRE-PROCESSING
prep = transforms.Compose([transforms.Resize(img_size),
                           transforms.ToTensor(),
                           transforms.Lambda(lambda x: x[torch.LongTensor([2, 1, 0])]), # CONVERT TO BGR FOR VGG
                           transforms.Normalize(mean = [0.40760392, 0.45795686, 0.48501961], std = [1, 1, 1]), # SUBTRACT IMAGENET MEAN
                           transforms.Lambda(lambda x: x.mul_(255)) # VGG WAS TRAINED WITH PIXEL VALUES 0-255
                           ])

# POST-PROCESSING A
postpa = transforms.Compose([transforms.Lambda(lambda x: x.mul_(1./255)), # REVERT EVERYTHING DONE IN THE PRE-PROCESSING STEP
                            transforms.Normalize(mean = [-0.40760392, -0.45795686, -0.48501961], std = [1, 1, 1]),
                            transforms.Lambda(lambda x: x[torch.LongTensor([2,1,0])])
                            ])

# POST-PROCESSING B
postpb = transforms.Compose([transforms.ToPILImage()])

# POST PROCESSING FUNCTION INCORPORATES A AND B, AND CLIPS PIXEL VALUES WHICH ARE OUT OF RANGE
def postp(tensor):
    t = postpa(tensor)
    t[t>1] = 1 # everything above 1 receives value 1
    t[t<0] = 0 # analogous for everything lower than 0
    img = postpb(t)
    return img



### PREPARING NETWORK ARCHITECTURE

vgg = VGG()

vgg.load_state_dict(torch.load(model_path))

for param in vgg.parameters():
    param.requires_grad = False

if torch.cuda.is_available():
    vgg.cuda()



### LOADING AND PREPARING IMAGES

img_paths = [image_path, image_path]

# IMAGE LOADING ORDER: [STYLE, CONTENT]
img_names = [sys.argv[1], sys.argv[2]]
imgs = [Image.open(img_paths[i] + name) for i, name in enumerate(img_names)]
imgs_torch = [prep(img) for img in imgs]

# HANDLE CUDA
if torch.cuda.is_available():
    imgs_torch = [Variable(img.unsqueeze(0)).cuda() for img in imgs_torch]
else:
    imgs_torch = [Variable(img.unsqueeze(0)) for img in imgs_torch]

style_img, content_img = imgs_torch

# SET UP IMAGE TO BE OPTIMIZED
# CAN BE INITIALIZED RANDOMLY
# OR AS A CLONE OF CONTENT IMAGE
opt_img = Variable(content_img.clone(), requires_grad = True)
print("Content size:", content_img.size(), sys.argv[2], "in", sys.argv[1])
print("Target size:", opt_img.size(), end="\n\n")



### SETUP FOR TRAINING

# LAYERS FOR STYLE AND CONTENT LOSS
style_layers = ['r11', 'r12', 'r31', 'r41', 'r51']
content_layers = ['r42']
loss_layers = style_layers + content_layers

# CREATING LOSS FUNCTION
loss_fns = [GramMSELoss()] * len(style_layers) + [nn.MSELoss()] * len(content_layers)
if torch.cuda.is_available():
    loss_fns = [loss_fn.cuda() for loss_fn in loss_fns]

# SETUP WEIGHTS FOR LOSS LAYERS
style_weights = [1e3/n**2 for n in [64, 128, 256, 512, 512]]
content_weights = [1e0]
weights = style_weights + content_weights

# CREATE OPTIMIZATION TARGETS
style_targets = [GramMatrix()(A).detach() for A in vgg(style_img, style_layers)]
content_targets = [A.detach() for A in vgg(content_img, content_layers)]
targets = style_targets + content_targets



### TRAINING LOOP

import numpy as np
from tqdm import tqdm

vis_factor = 10 # every 10 iterations, a frame snapshot is saved, we use this coeficient to scale
max_iter = 600 * vis_factor
show_iter = 1 * vis_factor

optimizer = optim.LBFGS([opt_img])
n_iter = [0]

image_array = []

with tqdm(total=max_iter, miniters=0, smoothing=0) as pbar:
    while n_iter[0] <= max_iter - 9: # weird behavior here

        def closure():
            optimizer.zero_grad()

            # FORWARD
            out = vgg(opt_img, loss_layers)

            # LOSS
            layer_losses = [weights[a] * loss_fns[a](A, targets[a]) for a,A in enumerate(out)]
            loss = sum(layer_losses)

            # BACKWARDS
            loss.backward()

            # TRACK PROGRESS
            if n_iter[0] % show_iter == 0:

                out_img = postp(opt_img.data[0].cpu().squeeze())
                image_array.append(np.array(out_img))

                pbar.update(show_iter)

            n_iter[0] += 1

            return loss

        optimizer.step(closure)

# SAVE ARRAY TO FILE

image_array = np.array(image_array)
np.save('images.npy', image_array)

print("")
