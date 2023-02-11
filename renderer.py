#!/bin/python

### very slow step that will be assigned to multiple
### jobs later in the development of this tool

### data loading

import numpy as np

image_array = np.load("images.npy", allow_pickle=True)

### progress bar

from tqdm import tqdm

pbar = tqdm(total = len(image_array))

### rendering of images

import matplotlib.pyplot as plt

def render(index):
    name = 'Output/neural_art_{:04d}.png'.format(index + 1)

    plt.axis('off')
    plt.imshow(image_array[index])
    plt.savefig(name, dpi=258, bbox_inches='tight', pad_inches=0) # dpi 258 -> 720p ; dpi 387 -> 1080p output image resolution
    plt.close('all')

for index in range(0, len(image_array)):
    render(index)
    pbar.update(1)
