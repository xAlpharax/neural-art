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

# wrap everything into a video (automatically overrides existing filenames)
#ffmpeg -y -framerate 60 -pattern_type glob -i 'Output/neural_art_*.png' -c:v libx264 -pix_fmt yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" $(basename ${2%.*})'_in_'$(basename ${1%.*})'.mp4' # H.264 all around
#ffmpeg -y -framerate 60 -pattern_type glob -i 'Output/neural_art_*.png' -c:v libsvtav1 -pix_fmt yuv420p  -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" $(basename ${2%.*})'_in_'$(basename ${1%.*})'.mp4' # AV1 weirddd
ffmpeg -y -framerate 60 -pattern_type glob -i 'Output/neural_art_*.png' -c:v libvpx-vp9 -pix_fmt yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" $(basename ${2%.*})'_in_'$(basename ${1%.*})'.mp4' # VP9 quality

# try -crf 10 (sane for vp9)
