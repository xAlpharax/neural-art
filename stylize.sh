#!/bin/bash

### You must be in the 'neural-art' directory when you run this

if [ $# -eq 2 ]
  then
    echo "Video file needs to be specified"
    exit 1
fi

# stylize data [pair (style, content)]
python neuralart.py $1 $2

# render images (actual frames) from images.npy
python renderer.py

# turn everything into a video
ffmpeg -framerate 60 -pattern_type glob -i 'Output/neural_art_*.png' -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" $3
