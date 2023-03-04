#!/bin/python

### data loading

import numpy as np

# will need some added functionality there for *.npy
image_array = np.load("images.npy")

### progress bar

from tqdm import tqdm
import sys

if len(sys.argv) == 1:
    pbar = tqdm(total=len(image_array), miniters=0, smoothing=0)

### image rendering from raw data

import matplotlib as mlp ; mlp.use('agg') ;
import matplotlib.pyplot as plt

dpi = 258 # dpi 258 -> 720p ; dpi 387 -> 1080p output image resolution

def render(index):
    pbar.update(1)

    name = 'Output/neural_art_{:04d}.png'.format(index + 1)

    plt.axis('off')
    plt.imshow(image_array[index])
    plt.savefig(name, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close('all')

### multi-threading

import os ; n_cores = os.cpu_count() // 2 ;

if len(sys.argv) == 1:
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=n_cores) as executor:
        executor.map(render, range(0, len(image_array)))

    exit()

if sys.argv[1] == "--fix":
    for index in range(0, 32):
        ### some artifacts may have slipped
        ### because of the thread pool
        name = 'Output/neural_art_{:04d}.png'.format(index + 1)

        plt.axis('off')
        plt.imshow(image_array[index])
        plt.savefig(name, dpi=dpi, bbox_inches='tight', pad_inches=0)
        plt.close('all')
