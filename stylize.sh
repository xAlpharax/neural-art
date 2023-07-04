#!/bin/bash

set -e ### exit the script if any part of it fails

cd "$(dirname "${BASH_SOURCE[0]}")"

cwd=$(pwd | sed -r 's%.*/%%g')
if [ $cwd != "neural-art" ] ; then
    echo "You must be in the 'neural-art' directory when you run this"
    exit 1
fi

if [ $# -eq 0 ] ; then
    echo "Style Image and Content Image need to be specified as arguments"
    echo "Example: ./stylize.sh Images/Jitter_Doll.jpg Images/cute.jpg"
    exit 1
fi

if [ $# -eq 1 ] ; then
    echo "Content image needs to be specified as well"
    echo "Example: ./stylize.sh Images/Jitter_Doll.jpg Images/cute.jpg"
    exit 1
fi

./clear_dir.sh # clear past checkpoint/realtime files

# stylize data [pair (style, content)]
python neuralart.py $1 $2

# render each image (actual frames) as per images.npy data
python renderer.py

# fix weird render artifacts
python renderer.py --fix

# wrap everything into a video (automatically overrides)
ffmpeg -y -framerate 60 -pattern_type glob -i 'Output/neural_art_*.png' -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" $(basename ${2%.*})'_in_'$(basename ${1%.*})'.mp4'
